import dataclasses
from typing import Optional, List, Any

from models.profile import UserProfile
from models.utils import from_union, from_list, from_none, to_class, from_bool, from_str, from_int


@dataclasses.dataclass
class DailyProfilesResponse:
    profiles: Optional[List[UserProfile]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DailyProfilesResponse':
        assert isinstance(obj, dict)
        if obj.get('profiles'):
            profiles = from_list(UserProfile.from_dict, obj.get('profiles'))
        else:
            profiles = None
        return DailyProfilesResponse(profiles)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.profiles is not None:
            result["profiles"] = from_union([lambda x: from_list(lambda y: to_class(UserProfile, y), x), from_none],
                                            self.profiles)
        return result


def daily_profiles_response_from_dict(s: Any) -> DailyProfilesResponse:
    return DailyProfilesResponse.from_dict(s)


def daily_profiles_response_to_dict(x: DailyProfilesResponse) -> Any:
    return to_class(DailyProfilesResponse, x)
