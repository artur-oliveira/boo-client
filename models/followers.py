import dataclasses
from typing import Optional, List, Any

from models.profile import UserProfile
from models.utils import from_union, from_list, from_none, to_class, from_bool, from_str, from_int


@dataclasses.dataclass
class FollowersResponse:
    followers: Optional[List[UserProfile]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FollowersResponse':
        assert isinstance(obj, dict)
        if obj.get('followers'):
            followers = from_list(UserProfile.from_dict, obj.get('followers'))
        else:
            followers = None
        return FollowersResponse(followers)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.followers is not None:
            result["followers"] = from_union([lambda x: from_list(lambda y: to_class(UserProfile, y), x), from_none],
                                             self.followers)
        return result


def followers_response_from_dict(s: Any) -> FollowersResponse:
    return FollowersResponse.from_dict(s)


def followers_response_to_dict(x: FollowersResponse) -> Any:
    return to_class(FollowersResponse, x)
