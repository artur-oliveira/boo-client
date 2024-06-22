import dataclasses
from typing import Optional, Any

from models.utils import from_union, from_str, from_none, is_type, to_class


@dataclasses.dataclass
class AuthRequest:
    grant_type: Optional[str] = dataclasses.field(default='refresh_token')
    refresh_token: Optional[str] = dataclasses.field(default=None)

    @staticmethod
    def from_dict(obj: Any) -> 'AuthRequest':
        assert isinstance(obj, dict)
        grant_type = from_union([from_str, from_none], obj.get("grantType"))
        refresh_token = from_union([from_str, from_none], obj.get("refreshToken"))
        return AuthRequest(grant_type, refresh_token)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.grant_type is not None:
            result["grantType"] = from_union([from_str, from_none], self.grant_type)
        if self.refresh_token is not None:
            result["refreshToken"] = from_union([from_str, from_none], self.refresh_token)
        return result


@dataclasses.dataclass
class AuthResponse:
    access_token: Optional[str] = None
    expires_in: Optional[int] = None
    token_type: Optional[str] = None
    refresh_token: Optional[str] = None
    id_token: Optional[str] = None
    user_id: Optional[str] = None
    project_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AuthResponse':
        assert isinstance(obj, dict)
        access_token = from_union([from_str, from_none], obj.get("access_token"))
        expires_in = from_union([from_none, lambda x: int(from_str(x))], obj.get("expires_in"))
        token_type = from_union([from_str, from_none], obj.get("token_type"))
        refresh_token = from_union([from_str, from_none], obj.get("refresh_token"))
        id_token = from_union([from_str, from_none], obj.get("id_token"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        project_id = from_union([from_str, from_none], obj.get("project_id"))
        return AuthResponse(access_token, expires_in, token_type, refresh_token, id_token, user_id, project_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.access_token is not None:
            result["access_token"] = from_union([from_str, from_none], self.access_token)
        if self.expires_in is not None:
            result["expires_in"] = from_union([lambda x: from_none((lambda y: is_type(type(None), y))(x)),
                                               lambda x: from_str((lambda y: str((lambda z: is_type(int, z))(y)))(x))],
                                              self.expires_in)
        if self.token_type is not None:
            result["token_type"] = from_union([from_str, from_none], self.token_type)
        if self.refresh_token is not None:
            result["refresh_token"] = from_union([from_str, from_none], self.refresh_token)
        if self.id_token is not None:
            result["id_token"] = from_union([from_str, from_none], self.id_token)
        if self.user_id is not None:
            result["user_id"] = from_union([from_str, from_none], self.user_id)
        if self.project_id is not None:
            result["project_id"] = from_union([from_str, from_none], self.project_id)
        return result


def auth_response_from_dict(s: Any) -> AuthResponse:
    return AuthResponse.from_dict(s)


def auth_response_to_dict(x: AuthResponse) -> Any:
    return to_class(AuthResponse, x)
