import dataclasses
from datetime import datetime
from typing import Any, List, Optional

from models.utils import from_union, from_str, from_none, from_list, to_class, from_int, from_datetime


@dataclasses.dataclass
class CreateMessage:
    user: Optional[str] = None
    text: Optional[str] = None
    created_at: Optional[datetime] = dataclasses.field(default_factory=datetime.now)

    @staticmethod
    def from_dict(obj: Any) -> 'CreateMessage':
        assert isinstance(obj, dict)
        user = from_union([from_str, from_none], obj.get("user"))
        text = from_union([from_str, from_none], obj.get("text"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        return CreateMessage(user, text, created_at)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user is not None:
            result["user"] = from_union([from_str, from_none], self.user)
        if self.text is not None:
            result["text"] = from_union([from_str, from_none], self.text)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        return result


@dataclasses.dataclass
class MessageResponse:
    id: Optional[str] = None
    chat: Optional[str] = None
    sender: Optional[str] = None
    text: Optional[str] = None
    created_at: Optional[datetime] = None
    quoted_message: Optional['MessageResponse'] = None
    v: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MessageResponse':
        assert isinstance(obj, dict)
        _id = from_union([from_str, from_none], obj.get("_id"))
        chat = from_union([from_str, from_none], obj.get("chat"))
        sender = from_union([from_str, from_none], obj.get("sender"))
        text = from_union([from_str, from_none], obj.get("text"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        quoted_message = from_union([MessageResponse.from_dict, from_none], obj.get("quotedMessage"))
        v = from_union([from_int, from_none], obj.get("__v"))
        return MessageResponse(_id, chat, sender, text, created_at, quoted_message, v)

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
        if self.quoted_message is not None:
            result["quotedMessage"] = from_union([lambda x: to_class(MessageResponse, x), from_none],
                                                 self.quoted_message)
        if self.v is not None:
            result["__v"] = from_union([from_int, from_none], self.v)
        return result


def message_response_from_dict(s: Any) -> List[MessageResponse]:
    return from_list(MessageResponse.from_dict, s)


def message_response_to_dict(data: List[MessageResponse]) -> Any:
    return from_list(lambda x: to_class(MessageResponse, x), data)
