import dataclasses
from typing import Optional

from models.awards import Award
from models.interest import Interest
from models.utils import *


@dataclasses.dataclass
class User:
    allow_incoming_requests: Optional[bool] = None
    follow_request_approved: Optional[bool] = None
    is_matched: Optional[bool] = None
    is_chat_expired: Optional[bool] = None
    dnd_post: Optional[bool] = None
    dnd_message: Optional[bool] = None
    stories: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        allow_incoming_requests = from_union([from_bool, from_none], obj.get("allowIncomingRequests"))
        follow_request_approved = from_union([from_bool, from_none], obj.get("followRequestApproved"))
        is_matched = from_union([from_bool, from_none], obj.get("isMatched"))
        is_chat_expired = from_union([from_bool, from_none], obj.get("isChatExpired"))
        dnd_post = from_union([from_bool, from_none], obj.get("dndPost"))
        dnd_message = from_union([from_bool, from_none], obj.get("dndMessage"))
        stories = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("stories"))
        return User(allow_incoming_requests, follow_request_approved, is_matched, is_chat_expired, dnd_post,
                    dnd_message, stories)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.allow_incoming_requests is not None:
            result["allowIncomingRequests"] = from_union([from_bool, from_none], self.allow_incoming_requests)
        if self.follow_request_approved is not None:
            result["followRequestApproved"] = from_union([from_bool, from_none], self.follow_request_approved)
        if self.is_matched is not None:
            result["isMatched"] = from_union([from_bool, from_none], self.is_matched)
        if self.is_chat_expired is not None:
            result["isChatExpired"] = from_union([from_bool, from_none], self.is_chat_expired)
        if self.dnd_post is not None:
            result["dndPost"] = from_union([from_bool, from_none], self.dnd_post)
        if self.dnd_message is not None:
            result["dndMessage"] = from_union([from_bool, from_none], self.dnd_message)
        if self.stories is not None:
            result["stories"] = from_union([lambda x: from_list(lambda y: y, x), from_none], self.stories)
        return result


@dataclasses.dataclass
class ProfileDetailResponse:
    user: Optional[User] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ProfileDetailResponse':
        assert isinstance(obj, dict)
        user = from_union([User.from_dict, from_none], obj.get("user"))
        return ProfileDetailResponse(user)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user is not None:
            result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        return result


@dataclasses.dataclass
class Gender(Enum):
    FEMALE = "female"


@dataclasses.dataclass
class InterestPoint:
    interest: Optional[str] = None
    language: Optional[str] = None
    points: Optional[int] = None
    rank: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InterestPoint':
        assert isinstance(obj, dict)
        interest = from_union([from_str, from_none], obj.get("interest"))
        language = from_union([from_str, from_none], obj.get("language"))
        points = from_union([from_int, from_none], obj.get("points"))
        rank = from_union([from_int, from_none], obj.get("rank"))
        return InterestPoint(interest, language, points, rank)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.interest is not None:
            result["interest"] = from_union([from_str, from_none], self.interest)
        if self.language is not None:
            result["language"] = from_union([from_str, from_none], self.language)
        if self.points is not None:
            result["points"] = from_union([from_int, from_none], self.points)
        if self.rank is not None:
            result["rank"] = from_union([from_int, from_none], self.rank)
        return result


class Drinking(Enum):
    FREQUENTLY = "Frequently"
    NEVER = "Never"
    SOBER = "Sober"
    SOCIALLY = "Socially"


class EducationLevel(Enum):
    HIGH_SCHOOL = "High school"
    IN_COLLEGE = "In college"
    GRADUATE_DEGREE = "Graduate degree"
    IN_GRAD_SCHOOL = "In grad school"
    TRADE_TECH_SCHOOL = "Trade/tech school"
    UNDERGRADUATE_DEGREE = "Undergraduate degree"


class Exercise(Enum):
    ACTIVE = "Active"
    ALMOST_NEVER = "Almost never"
    SOMETIMES = "Sometimes"


class Kids(Enum):
    DON_T_WANT = "Don't want"
    HAVE_DON_T_WANT_MORE = "Have & don't want more"
    HAVE_WANT_MORE = "Have & want more"
    NOT_SURE_YET = "Not sure yet"
    WANT_SOMEDAY = "Want someday"


class Smoking(Enum):
    NEVER = "Never"
    REGULARLY = "Regularly"
    SOCIALLY = "Socially"


class Religion(Enum):
    ATHEIST = 'Atheist'
    AGNOSTIC = "Agnostic"
    CATHOLIC = "Catholic"
    CHRISTIAN = "Christian"
    OTHER = "Other"
    SPIRITUAL = "Spiritual"
    MORMON = "Mormon"
    BUDDHIST = "Buddhist"


@dataclasses.dataclass
class MoreAboutUser:
    smoking: Optional[Smoking] = None
    drinking: Optional[Drinking] = None
    religion: Optional[Religion] = None
    exercise: Optional[Exercise] = None
    education_level: Optional[EducationLevel] = None
    kids: Optional[Kids] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MoreAboutUser':
        assert isinstance(obj, dict)
        smoking = from_union([Smoking, from_none], obj.get("smoking"))
        drinking = from_union([Drinking, from_none], obj.get("drinking"))
        religion = from_union([Religion, from_none], obj.get("religion"))
        exercise = from_union([Exercise, from_none], obj.get("exercise"))
        education_level = from_union([EducationLevel, from_none], obj.get("educationLevel"))
        kids = from_union([Kids, from_none], obj.get("kids"))
        return MoreAboutUser(smoking, drinking, religion, exercise, education_level, kids)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.smoking is not None:
            result["smoking"] = from_union([lambda x: to_enum(Smoking, x), from_none], self.smoking)
        if self.drinking is not None:
            result["drinking"] = from_union([lambda x: to_enum(Drinking, x), from_none], self.drinking)
        if self.religion is not None:
            result["religion"] = from_union([lambda x: to_enum(Religion, x), from_none], self.religion)
        if self.exercise is not None:
            result["exercise"] = from_union([lambda x: to_enum(Exercise, x), from_none], self.exercise)
        if self.education_level is not None:
            result["educationLevel"] = from_union([lambda x: to_enum(EducationLevel, x), from_none],
                                                  self.education_level)
        if self.kids is not None:
            result["kids"] = from_union([lambda x: to_enum(Kids, x), from_none], self.kids)
        return result


@dataclasses.dataclass
class Personality:
    mbti: Optional[str] = None
    avatar: Optional[str] = None
    ei: Optional[float] = None
    ns: Optional[float] = None
    ft: Optional[float] = None
    jp: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Personality':
        assert isinstance(obj, dict)
        mbti = from_union([from_str, from_none], obj.get("mbti"))
        avatar = from_union([from_str, from_none], obj.get("avatar"))
        ei = from_union([from_float, from_none], obj.get("EI"))
        ns = from_union([from_float, from_none], obj.get("NS"))
        ft = from_union([from_float, from_none], obj.get("FT"))
        jp = from_union([from_float, from_none], obj.get("JP"))
        return Personality(mbti, avatar, ei, ns, ft, jp)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.mbti is not None:
            result["mbti"] = from_union([from_str, from_none], self.mbti)
        if self.avatar is not None:
            result["avatar"] = from_union([from_str, from_none], self.avatar)
        if self.ei is not None:
            result["EI"] = from_union([to_float, from_none], self.ei)
        if self.ns is not None:
            result["NS"] = from_union([to_float, from_none], self.ns)
        if self.ft is not None:
            result["FT"] = from_union([to_float, from_none], self.ft)
        if self.jp is not None:
            result["JP"] = from_union([to_float, from_none], self.jp)
        return result


class Purpose(Enum):
    DATING = "dating"
    FRIENDS = "friends"


@dataclasses.dataclass
class Preferences:
    show_to_verified_only: Optional[bool] = None
    purpose: Optional[List[Purpose]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Preferences':
        assert isinstance(obj, dict)
        show_to_verified_only = from_union([from_bool, from_none], obj.get("showToVerifiedOnly"))
        purpose = from_union([lambda x: from_list(Purpose, x), from_none], obj.get("purpose"))
        return Preferences(show_to_verified_only, purpose)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.show_to_verified_only is not None:
            result["showToVerifiedOnly"] = from_union([from_bool, from_none], self.show_to_verified_only)
        if self.purpose is not None:
            result["purpose"] = from_union([lambda x: from_list(lambda y: to_enum(Purpose, y), x), from_none],
                                           self.purpose)
        return result


@dataclasses.dataclass
class Prompt:
    id: Optional[int] = None
    answer: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Prompt':
        assert isinstance(obj, dict)
        _id = from_union([from_none, lambda x: int(from_str(x))], obj.get("id"))
        answer = from_union([from_str, from_none], obj.get("answer"))
        return Prompt(_id, answer)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([lambda x: from_none((lambda y: is_type(type(None), y))(x)),
                                       lambda x: from_str((lambda y: str((lambda z: is_type(int, z))(y)))(x))], self.id)
        if self.answer is not None:
            result["answer"] = from_union([from_str, from_none], self.answer)
        return result


class Timezone(Enum):
    AMERICA_BAHIA = "America/Bahia"
    AMERICA_FORTALEZA = "America/Fortaleza"
    AMERICA_MANAUS = "America/Manaus"
    AMERICA_SAO_PAULO = "America/Sao_Paulo"
    ASIA_SHANGAI = "Asia/Shanghai"
    AMERICA_BELEM = "America/Belem"
    AMERICA_NEW_YORK = "America/New_York"
    AMERICA_RECIFE = "America/Recife"
    AMERICA_ARAGUAINA = "America/Araguaina"
    AMERICA_RIO_BRANCO = "America/Rio_Branco"
    AMERICA_BOA_VISTA = "America/Boa_Vista"
    ETC_GMT_3 = "Etc/GMT+3"


class VerificationStatus(Enum):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"


@dataclasses.dataclass
class UserProfile:
    id: Optional[str] = None
    first_name: Optional[str] = None
    pictures: Optional[List[str]] = None
    profile_picture: Optional[str] = None
    personality: Optional[Personality] = None
    gender: Optional[Gender] = None
    age: Optional[int] = None
    height: Optional[int] = None
    ethnicities: Optional[List[str]] = None
    description: Optional[str] = None
    education: Optional[str] = None
    work: Optional[str] = None
    more_about_user: Optional[MoreAboutUser] = None
    prompts: Optional[List[Prompt]] = None
    crown: Optional[bool] = None
    handle: Optional[str] = None
    location: Optional[str] = None
    teleport: Optional[bool] = None
    preferences: Optional[Preferences] = None
    hide_questions: Optional[bool] = None
    hide_comments: Optional[bool] = None
    horoscope: Optional[str] = None
    interests: Optional[List[Interest]] = None
    interest_names: Optional[List[str]] = None
    karma: Optional[int] = None
    num_followers: Optional[int] = None
    verified: Optional[bool] = None
    verification_status: Optional[VerificationStatus] = None
    languages: Optional[List[str]] = None
    timezone: Optional[Timezone] = None
    hidden: Optional[bool] = None
    interest_points: Optional[List[InterestPoint]] = None
    enneagram: Optional[str] = None
    awards: Optional[Award] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserProfile':
        assert isinstance(obj, dict)
        _id = from_union([from_str, from_none], obj.get("_id"))
        first_name = from_union([from_str, from_none], obj.get("firstName"))
        pictures = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pictures"))
        profile_picture = from_union([from_str, from_none], obj.get("profilePicture"))
        personality = from_union([Personality.from_dict, from_none], obj.get("personality"))
        gender = from_union([Gender, from_none], obj.get("gender"))
        age = from_union([from_int, from_none], obj.get("age"))
        height = from_union([from_int, from_none], obj.get("height"))
        ethnicities = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ethnicities"))
        description = from_union([from_str, from_none], obj.get("description"))
        education = from_union([from_str, from_none], obj.get("education"))
        work = from_union([from_str, from_none], obj.get("work"))
        more_about_user = from_union([MoreAboutUser.from_dict, from_none], obj.get("moreAboutUser"))
        prompts = from_union([lambda x: from_list(Prompt.from_dict, x), from_none], obj.get("prompts"))
        crown = from_union([from_bool, from_none], obj.get("crown"))
        handle = from_union([from_str, from_none], obj.get("handle"))
        location = from_union([from_none, from_str], obj.get("location"))
        teleport = from_union([from_bool, from_none], obj.get("teleport"))
        preferences = from_union([Preferences.from_dict, from_none], obj.get("preferences"))
        hide_questions = from_union([from_bool, from_none], obj.get("hideQuestions"))
        hide_comments = from_union([from_bool, from_none], obj.get("hideComments"))
        horoscope = from_union([from_str, from_none], obj.get("horoscope"))
        interests = from_union([lambda x: from_list(Interest.from_dict, x), from_none], obj.get("interests"))
        interest_names = from_union([lambda x: from_list(from_str, x), from_none], obj.get("interestNames"))
        karma = from_union([from_int, from_none], obj.get("karma"))
        num_followers = from_union([from_int, from_none], obj.get("numFollowers"))
        verified = from_union([from_bool, from_none], obj.get("verified"))
        verification_status = from_union([VerificationStatus, from_none], obj.get("verificationStatus"))
        languages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("languages"))
        timezone = from_union([Timezone, from_none], obj.get("timezone"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        interest_points = from_union([lambda x: from_list(InterestPoint.from_dict, x), from_none],
                                     obj.get("interestPoints"))
        enneagram = from_union([from_str, from_none], obj.get("enneagram"))
        awards = from_union([Award.from_dict, from_none], obj.get("awards"))
        return UserProfile(_id, first_name, pictures, profile_picture, personality, gender, age, height, ethnicities,
                           description, education, work, more_about_user, prompts, crown, handle, location, teleport,
                           preferences, hide_questions, hide_comments, horoscope, interests, interest_names, karma,
                           num_followers, verified, verification_status, languages, timezone, hidden, interest_points,
                           enneagram, awards)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["_id"] = from_union([from_str, from_none], self.id)
        if self.first_name is not None:
            result["firstName"] = from_union([from_str, from_none], self.first_name)
        if self.pictures is not None:
            result["pictures"] = from_union([lambda x: from_list(from_str, x), from_none], self.pictures)
        if self.profile_picture is not None:
            result["profilePicture"] = from_union([from_str, from_none], self.profile_picture)
        if self.personality is not None:
            result["personality"] = from_union([lambda x: to_class(Personality, x), from_none], self.personality)
        if self.gender is not None:
            result["gender"] = from_union([lambda x: to_enum(Gender, x), from_none], self.gender)
        if self.age is not None:
            result["age"] = from_union([from_int, from_none], self.age)
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        if self.ethnicities is not None:
            result["ethnicities"] = from_union([lambda x: from_list(from_str, x), from_none], self.ethnicities)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.education is not None:
            result["education"] = from_union([from_str, from_none], self.education)
        if self.enneagram is not None:
            result["enneagram"] = from_union([from_str, from_none], self.enneagram)
        if self.more_about_user is not None:
            result["moreAboutUser"] = from_union([lambda x: to_class(MoreAboutUser, x), from_none],
                                                 self.more_about_user)
        if self.prompts is not None:
            result["prompts"] = from_union([lambda x: from_list(lambda y: to_class(Prompt, y), x), from_none],
                                           self.prompts)
        if self.crown is not None:
            result["crown"] = from_union([from_none, from_bool], self.crown)
        if self.location is not None:
            result["location"] = from_union([from_str, from_none], self.location)
        if self.teleport is not None:
            result["teleport"] = from_union([from_none, from_bool], self.teleport)
        if self.preferences is not None:
            result["preferences"] = from_union([lambda x: to_class(Preferences, x), from_none], self.preferences)
        if self.hide_questions is not None:
            result["hideQuestions"] = from_union([from_none, from_bool], self.hide_questions)
        if self.hide_comments is not None:
            result["hideComments"] = from_union([from_none, from_bool], self.hide_comments)
        if self.horoscope is not None:
            result["horoscope"] = from_union([from_str, from_none], self.horoscope)
        if self.interests is not None:
            result["interests"] = from_union([lambda x: from_list(lambda y: to_class(Interest, y), x), from_none],
                                             self.interests)
        if self.interest_names is not None:
            result["interestNames"] = from_union([lambda x: from_list(from_str, x), from_none], self.interest_names)
        if self.karma is not None:
            result["karma"] = from_union([from_int, from_none], self.karma)
        if self.num_followers is not None:
            result["numFollowers"] = from_union([from_int, from_none], self.num_followers)
        if self.verified is not None:
            result["verified"] = from_union([from_none, from_bool], self.verified)
        if self.verification_status is not None:
            result["verificationStatus"] = from_union([lambda x: to_enum(VerificationStatus, x), from_none],
                                                      self.verification_status)
        if self.languages is not None:
            result["languages"] = from_union([lambda x: from_list(from_str, x), from_none], self.languages)
        if self.timezone is not None:
            result["timezone"] = from_union([lambda x: to_enum(Timezone, x), from_none], self.timezone)
        if self.hidden is not None:
            result["hidden"] = from_union([from_none, from_bool], self.hidden)
        if self.interest_points is not None:
            result["interestPoints"] = from_union(
                [lambda x: from_list(lambda y: to_class(InterestPoint, y), x), from_none], self.interest_points)
        if self.handle is not None:
            result["handle"] = from_union([from_str, from_none], self.handle)
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        if self.work is not None:
            result["work"] = from_union([from_str, from_none], self.work)
        return result
