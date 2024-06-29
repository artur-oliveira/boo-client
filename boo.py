import dataclasses
import os
from typing import Any, List

import requests

from constants import API_BOO_HOST, CDN_BOO_HOST, GOOGLE_AUTH_URL, BOO_KEY_GOOGLE
from exceptions import BooClientException
from http_utils import http_session
from models.authentication import AuthRequest, AuthResponse
from models.chats import ChatsResponse
from models.daily_profiles import DailyProfilesResponse
from models.init_app import InitAppResponse, InitAppRequest
from models.messages import MessageResponse, message_response_from_dict, CreateMessage
from models.profile import ProfileDetailResponse, UserProfile
from models.questions import QuestionsResponse


@dataclasses.dataclass
class BooClient:
    refresh_token: str = dataclasses.field()
    auth: AuthResponse = dataclasses.field(default=None)
    _session: requests.Session = dataclasses.field(default_factory=http_session)

    def json_headers(self) -> dict:
        return {
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/json',
            'Authorization': f'{self.auth.access_token}',
            'User-Agent': 'Dart/3.3 (dart:io)'
        }

    def __post_init__(self):
        self.auth = self.authenticate(AuthRequest(
            refresh_token=self.refresh_token
        ))

    def init_app(self, init_app_request: InitAppRequest) -> InitAppResponse:
        res = self._session.put(
            url=f'{API_BOO_HOST}/v1/user/initApp',
            headers=self.json_headers(),
            json=dataclasses.asdict(init_app_request)
        )
        if not res.ok:
            raise BooClientException(res.content)
        return InitAppResponse.from_dict(res.json())

    def authenticate(self, auth_request: AuthRequest) -> AuthResponse:
        res = self._session.post(
            url=f'{GOOGLE_AUTH_URL}',
            json=auth_request.to_dict(),
            params=dict(key=BOO_KEY_GOOGLE)
        )
        if not res.ok:
            raise BooClientException(res.content)
        return AuthResponse.from_dict(res.json())

    def _chats(self, chat_type, query_params: dict | None = None) -> ChatsResponse:
        res = self._session.get(
            url=f'{API_BOO_HOST}/v1/chat/{chat_type}',
            params=query_params,
            headers=self.json_headers(),
        )
        if not res.ok:
            raise BooClientException(res.content)
        return ChatsResponse.from_dict(res.json())

    def sent_chats(self, before: str = '') -> ChatsResponse:
        return self._chats(chat_type='sent', query_params=dict(before=before))

    def pending_chats(self, before: str = '') -> ChatsResponse:
        return self._chats(chat_type='pending', query_params=dict(before=before))

    def messaged_chats(self, before: str = '') -> ChatsResponse:
        return self._chats(chat_type='messaged', query_params=dict(before=before))

    @classmethod
    def _all_chats(cls, chats_f) -> ChatsResponse:
        all_chats_response = ChatsResponse(chats=[])
        before = ''
        while True:
            sent_chats = chats_f(before=before)
            all_chats_response.chats.extend(sent_chats.chats)
            before = sent_chats.last_chat_message_time()
            if len(sent_chats.chats) < 20:
                break
        return all_chats_response

    def all_sent_chats(self) -> ChatsResponse:
        return self._all_chats(chats_f=self.sent_chats)

    def all_messaged_chats(self) -> ChatsResponse:
        return self._all_chats(chats_f=self.messaged_chats)

    def all_pending_chats(self) -> ChatsResponse:
        return self._all_chats(chats_f=self.pending_chats)

    def messages(self, chat_id, user_id) -> List[MessageResponse]:
        res = self._session.get(
            url=f'{API_BOO_HOST}/v1/message',
            params=dict(user=user_id, chatId=chat_id),
            headers=self.json_headers(),
        )
        if not res.ok:
            raise BooClientException(res.content)
        return message_response_from_dict(res.json())

    def create_message(self, chat_id: str, quoted_message_id: str, message: CreateMessage) -> MessageResponse:
        res = self._session.post(
            url=f'{API_BOO_HOST}/v1/message',
            headers=self.json_headers(),
            json=message.to_dict(),
            params=dict(chatId=chat_id, quotedMessageId=quoted_message_id),
        )
        if not res.ok:
            raise BooClientException(res.content.decode('utf-8'))
        return MessageResponse.from_dict(res.json())

    def questions(self, user_id: str, before_question_id: str = '', sort: str = 'popular') -> QuestionsResponse:
        res = self._session.get(
            url=f'{API_BOO_HOST}/v1/user/questions',
            params=dict(createdBy=user_id, beforeId=before_question_id, sort=sort),
            headers=self.json_headers(),
        )
        if not res.ok:
            raise BooClientException(res.content)
        return QuestionsResponse.from_dict(res.json())

    def media(self, media_id) -> Any:
        res = self._session.get(
            url=f'{CDN_BOO_HOST}/{media_id}',
            headers=self.json_headers(),
        )
        if not res.ok:
            raise BooClientException(res.content)
        return res.content

    def profile_detail(self, user_id) -> ProfileDetailResponse:
        res = self._session.get(
            url=f'{API_BOO_HOST}/v1/user/profileDetails',
            headers=self.json_headers(),

            params=dict(user=user_id),
        )
        if not res.ok:
            raise BooClientException(res.content.decode('utf-8'))
        return ProfileDetailResponse.from_dict(res.json())

    def daily_profiles(self) -> DailyProfilesResponse:
        res = self._session.get(
            url=f'{API_BOO_HOST}/v1/user/dailyProfiles',
            headers=self.json_headers()
        )
        if not res.ok:
            raise BooClientException(res.content.decode('utf-8'))
        return DailyProfilesResponse.from_dict(res.json())

    def like(self, user_id) -> None:
        res = self._session.patch(
            url=f'{API_BOO_HOST}/v1/user/sendLike',
            headers=self.json_headers(),
            json=dict(user=user_id)
        )
        if not res.ok:
            raise BooClientException(res.content.decode('utf-8'))

    def not_like(self, user_id) -> None:
        res = self._session.patch(
            url=f'{API_BOO_HOST}/v1/user/pass',
            headers=self.json_headers(),
            json=dict(user=user_id)
        )
        if not res.ok:
            raise BooClientException(res.content.decode('utf-8'))

    def download_media(self, media_id: str, media_name: str | None = None, to_folder='media') -> str:
        if not to_folder.endswith('/'):
            to_folder += '/'
        if not media_name:
            media_name = media_id.replace('/', '_')
        file_name = f'{to_folder}{media_name}'
        if not os.path.exists(to_folder):
            os.makedirs(to_folder)
        with open(file_name, 'wb') as media:
            media.write(self.media(media_id))
        return media_name

    def download_profile_pictures(self, profile: UserProfile) -> None:
        for picture in profile.pictures:
            self.download_media(picture, to_folder=f'media/{profile.id}_{profile.first_name}')

    def like_daily_profiles(self, quantity: int = 20):
        liked = []
        while len(liked) < quantity:
            profs = self.daily_profiles()
            for prof in profs.profiles:
                self.like(prof.id)
                liked.append(prof.id)


if __name__ == '__main__':
    refresh_token = os.getenv('REFRESH_TOKEN')
    if not refresh_token:
        raise BooClientException('you cant use boo client without an refresh token')
    client = BooClient(
        refresh_token=refresh_token
    )
    messaged = client.all_messaged_chats()
    for chat in messaged.chats:
        client.download_profile_pictures(chat.user)
    print(len(messaged.chats))
