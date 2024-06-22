import dataclasses
from typing import Optional

from models.profile import UserProfile
from models.utils import *


@dataclasses.dataclass
class QuotedStory:
    id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QuotedStory':
        assert isinstance(obj, dict)
        _id = from_union([from_str, from_none], obj.get("_id"))
        return QuotedStory(_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["_id"] = from_union([from_str, from_none], self.id)
        return result


@dataclasses.dataclass
class LastMessage:
    id: Optional[str] = None
    chat: Optional[str] = None
    sender: Optional[str] = None
    text: Optional[str] = None
    created_at: Optional[datetime] = None
    v: Optional[int] = None
    quoted_story: Optional[QuotedStory] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LastMessage':
        assert isinstance(obj, dict)
        _id = from_union([from_str, from_none], obj.get("_id"))
        chat = from_union([from_str, from_none], obj.get("chat"))
        sender = from_union([from_str, from_none], obj.get("sender"))
        text = from_union([from_str, from_none], obj.get("text"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        v = from_union([from_int, from_none], obj.get("__v"))
        quoted_story = from_union([QuotedStory.from_dict, from_none], obj.get("quotedStory"))
        return LastMessage(_id, chat, sender, text, created_at, v, quoted_story)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["_id"] = from_union([from_str, from_none], self.id)
        if self.chat is not None:
            result["chat"] = from_union([from_str, from_none], self.chat)
        if self.sender is not None:
            result["sender"] = from_union([from_str, from_none], self.sender)
        if self.text is not None:
            result["text"] = from_union([from_str, from_none], self.text)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.v is not None:
            result["__v"] = from_union([from_int, from_none], self.v)
        if self.quoted_story is not None:
            result["quotedStory"] = from_union([lambda x: to_class(QuotedStory, x), from_none], self.quoted_story)
        return result


@dataclasses.dataclass
class Chat:
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    users: Optional[List[UserProfile]] = None
    user: Optional[UserProfile] = None
    last_message: Optional[LastMessage] = None
    last_message_time: Optional[datetime] = None
    num_messages: Optional[int] = None
    num_unread_messages: Optional[int] = None
    partner_num_unread_messages: Optional[int] = None
    pending_user: Optional[str] = None
    expiration_date: Optional[datetime] = None
    muted: Optional[bool] = None
    dnd_message: Optional[bool] = None
    dnd_post: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Chat':
        assert isinstance(obj, dict)
        _id = from_union([from_str, from_none], obj.get("_id"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        if obj.get('users'):
            users = from_list(UserProfile.from_dict, obj.get('users'))
        else:
            users = None
        user = from_union([UserProfile.from_dict, from_none], obj.get("user"))
        last_message = from_union([LastMessage.from_dict, from_none], obj.get("lastMessage"))
        last_message_time = from_union([from_datetime, from_none], obj.get("lastMessageTime"))
        num_messages = from_union([from_int, from_none], obj.get("numMessages"))
        num_unread_messages = from_union([from_int, from_none], obj.get("numUnreadMessages"))
        partner_num_unread_messages = from_union([from_int, from_none], obj.get("partnerNumUnreadMessages"))
        pending_user = from_union([from_str, from_none], obj.get("pendingUser"))
        expiration_date = from_union([from_datetime, from_none], obj.get("expirationDate"))
        muted = from_union([from_none, from_bool], obj.get("muted"))
        dnd_message = from_union([from_none, from_bool], obj.get("dndMessage"))
        dnd_post = from_union([from_none, from_bool], obj.get("dndPost"))
        return Chat(_id, created_at, users, user, last_message, last_message_time, num_messages, num_unread_messages,
                    partner_num_unread_messages, pending_user, expiration_date, muted, dnd_message, dnd_post)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["_id"] = from_union([from_str, from_none], self.id)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.users is not None:
            result["users"] = from_union([lambda x: from_list(lambda y: to_class(UserProfile, y), x), from_none],
                                         self.users)
        if self.user is not None:
            result["user"] = from_union([lambda x: to_class(UserProfile, x), from_none], self.user)
        if self.last_message is not None:
            result["lastMessage"] = from_union([lambda x: to_class(LastMessage, x), from_none], self.last_message)
        if self.last_message_time is not None:
            result["lastMessageTime"] = from_union([lambda x: x.isoformat(), from_none], self.last_message_time)
        if self.num_messages is not None:
            result["numMessages"] = from_union([from_int, from_none], self.num_messages)
        if self.num_unread_messages is not None:
            result["numUnreadMessages"] = from_union([from_int, from_none], self.num_unread_messages)
        if self.partner_num_unread_messages is not None:
            result["partnerNumUnreadMessages"] = from_union([from_int, from_none], self.partner_num_unread_messages)
        if self.pending_user is not None:
            result["pendingUser"] = from_union([from_str, from_none], self.pending_user)
        if self.expiration_date is not None:
            result["expirationDate"] = from_union([lambda x: x.isoformat(), from_none], self.expiration_date)
        if self.muted is not None:
            result["muted"] = from_union([from_none, from_bool], self.muted)
        if self.dnd_message is not None:
            result["dndMessage"] = from_union([from_none, from_bool], self.dnd_message)
        if self.dnd_post is not None:
            result["dndPost"] = from_union([from_none, from_bool], self.dnd_post)
        return result


@dataclasses.dataclass
class ChatsResponse:
    chats: Optional[List[Chat]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ChatsResponse':
        assert isinstance(obj, dict)
        if obj.get('chats'):
            chats = from_list(Chat.from_dict, obj.get('chats'))
        else:
            chats = None

        return ChatsResponse(chats)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.chats is not None:
            result["chats"] = from_union([lambda x: from_list(lambda y: to_class(Chat, y), x), from_none], self.chats)
        return result

    def last_chat_message_time(self) -> str:
        last_chat = self.chats[len(self.chats) - 1] if self.chats else None
        if not last_chat:
            return ''
        micro_sec = int(last_chat.last_message_time.strftime("%f").rstrip('0'))
        return last_chat.last_message_time.strftime(f"%Y-%m-%dT%H:%M:%S.{micro_sec}Z")


def chats_from_dict(s: Any) -> ChatsResponse:
    return ChatsResponse.from_dict(s)


def chats_to_dict(x: ChatsResponse) -> Any:
    return to_class(ChatsResponse, x)
