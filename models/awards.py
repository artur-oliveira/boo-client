import dataclasses
from enum import Enum
from typing import Optional, Any

from models.utils import from_union, from_int, from_str, from_none, to_enum


class TypeEnum(Enum):
    PREMIUM = "premium"
    REGULAR = "regular"


@dataclasses.dataclass
class Award:
    id: Optional[str] = None
    price: Optional[int] = None
    reward: Optional[int] = None
    type: Optional[TypeEnum] = None
    name: Optional[str] = None
    description: Optional[str] = None
    color: Optional[str] = None
    the_100: Optional[int] = None
    heart: Optional[int] = None
    cake: Optional[int] = None
    rainbow: Optional[int] = None
    shocked_surprise: Optional[int] = None
    handshake: Optional[int] = None
    cool: Optional[int] = None
    peek_a_boo: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Award':
        assert isinstance(obj, dict)
        _id = from_union([from_str, from_none], obj.get("id"))
        price = from_union([from_int, from_none], obj.get("price"))
        reward = from_union([from_int, from_none], obj.get("reward"))
        _type = from_union([TypeEnum, from_none], obj.get("type"))
        name = from_union([from_str, from_none], obj.get("name"))
        description = from_union([from_str, from_none], obj.get("description"))
        color = from_union([from_str, from_none], obj.get("color"))
        return Award(_id, price, reward, _type, name, description, color)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.price is not None:
            result["price"] = from_union([from_int, from_none], self.price)
        if self.reward is not None:
            result["reward"] = from_union([from_int, from_none], self.reward)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(TypeEnum, x), from_none], self.type)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.color is not None:
            result["color"] = from_union([from_str, from_none], self.color)
        return result
