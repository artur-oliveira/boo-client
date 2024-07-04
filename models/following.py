import dataclasses
from typing import Optional, List, Any

from models.profile import UserProfile
from models.utils import from_union, from_list, from_none, to_class, from_bool, from_str, from_int


@dataclasses.dataclass
class FollowingResponse:
    following: Optional[List[UserProfile]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FollowingResponse':
        assert isinstance(obj, dict)
        if obj.get('following'):
            following = from_list(UserProfile.from_dict, obj.get('following'))
        else:
            following = None
        return FollowingResponse(following)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.following is not None:
            result["following"] = from_union([lambda x: from_list(lambda y: to_class(UserProfile, y), x), from_none],
                                             self.following)
        return result


def following_response_from_dict(s: Any) -> FollowingResponse:
    return FollowingResponse.from_dict(s)


def following_response_to_dict(x: FollowingResponse) -> Any:
    return to_class(FollowingResponse, x)
