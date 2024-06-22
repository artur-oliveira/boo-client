import dataclasses
from typing import Optional

from constants import *
from models.awards import Award
from models.utils import *


@dataclasses.dataclass
class InitAppRequest:
    appVersion: str = dataclasses.field(default=APP_VERSION)
    timezone: str = dataclasses.field(default=TZ)
    locale: str = dataclasses.field(default=LOCALE)
    countryLocale: str = dataclasses.field(default=COUNTRY_LOCALE)
    app_instance_id: str = dataclasses.field(default=APP_INSTANCE_ID)
    advertisingId: str = dataclasses.field(default=ADVERTISING_ID)
    deviceLanguage: str = dataclasses.field(default=DEVICE_LANGUAGE)
    os: str = dataclasses.field(default=OS_ANDROID)
    osVersion: str = dataclasses.field(default=OS_ANDROID_VERSION)
    phoneModel: str = dataclasses.field(default=PHONE_MODEL)
    deviceId: str = dataclasses.field(default=DEVICE_ID)
    isPhysicalDevice: bool = dataclasses.field(default=True)


@dataclasses.dataclass
class Boost:
    price: Optional[int] = None
    duration_minutes: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Boost':
        assert isinstance(obj, dict)
        price = from_union([from_int, from_none], obj.get("price"))
        duration_minutes = from_union([from_int, from_none], obj.get("durationMinutes"))
        return Boost(price, duration_minutes)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.price is not None:
            result["price"] = from_union([from_int, from_none], self.price)
        if self.duration_minutes is not None:
            result["durationMinutes"] = from_union([from_int, from_none], self.duration_minutes)
        return result


@dataclasses.dataclass
class BoostPost:
    price: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BoostPost':
        assert isinstance(obj, dict)
        price = from_union([from_int, from_none], obj.get("price"))
        return BoostPost(price)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.price is not None:
            result["price"] = from_union([from_int, from_none], self.price)
        return result


@dataclasses.dataclass
class Gift:
    id: Optional[int] = None
    price: Optional[int] = None
    emoji: Optional[str] = None
    caption: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Gift':
        assert isinstance(obj, dict)
        _id = from_union([from_none, lambda x: int(from_str(x))], obj.get("id"))
        price = from_union([from_none, lambda x: int(from_str(x))], obj.get("price"))
        emoji = from_union([from_str, from_none], obj.get("emoji"))
        caption = from_union([from_str, from_none], obj.get("caption"))
        return Gift(_id, price, emoji, caption)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([lambda x: from_none((lambda y: is_type(type(None), y))(x)),
                                       lambda x: from_str((lambda y: str((lambda z: is_type(int, z))(y)))(x))], self.id)
        if self.price is not None:
            result["price"] = from_union([lambda x: from_none((lambda y: is_type(type(None), y))(x)),
                                          lambda x: from_str((lambda y: str((lambda z: is_type(int, z))(y)))(x))],
                                         self.price)
        if self.emoji is not None:
            result["emoji"] = from_union([from_str, from_none], self.emoji)
        if self.caption is not None:
            result["caption"] = from_union([from_str, from_none], self.caption)
        return result


@dataclasses.dataclass
class CoinProducts:
    direct_message: Optional[BoostPost] = None
    revival: Optional[BoostPost] = None
    rewind: Optional[BoostPost] = None
    boost: Optional[Boost] = None
    boost_post: Optional[BoostPost] = None
    level_up: Optional[Boost] = None
    view_last_seen: Optional[BoostPost] = None
    sticker_pack: Optional[BoostPost] = None
    reactivate_chat: Optional[BoostPost] = None
    gifts: Optional[List[Gift]] = None
    awards: Optional[List[Award]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CoinProducts':
        assert isinstance(obj, dict)
        direct_message = from_union([BoostPost.from_dict, from_none], obj.get("directMessage"))
        revival = from_union([BoostPost.from_dict, from_none], obj.get("revival"))
        rewind = from_union([BoostPost.from_dict, from_none], obj.get("rewind"))
        boost = from_union([Boost.from_dict, from_none], obj.get("boost"))
        boost_post = from_union([BoostPost.from_dict, from_none], obj.get("boostPost"))
        level_up = from_union([Boost.from_dict, from_none], obj.get("levelUp"))
        view_last_seen = from_union([BoostPost.from_dict, from_none], obj.get("viewLastSeen"))
        sticker_pack = from_union([BoostPost.from_dict, from_none], obj.get("stickerPack"))
        reactivate_chat = from_union([BoostPost.from_dict, from_none], obj.get("reactivateChat"))
        gifts = from_union([lambda x: from_list(Gift.from_dict, x), from_none], obj.get("gifts"))
        awards = from_union([lambda x: from_list(Award.from_dict, x), from_none], obj.get("awards"))
        return CoinProducts(direct_message, revival, rewind, boost, boost_post, level_up, view_last_seen, sticker_pack,
                            reactivate_chat, gifts, awards)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.direct_message is not None:
            result["directMessage"] = from_union([lambda x: to_class(BoostPost, x), from_none], self.direct_message)
        if self.revival is not None:
            result["revival"] = from_union([lambda x: to_class(BoostPost, x), from_none], self.revival)
        if self.rewind is not None:
            result["rewind"] = from_union([lambda x: to_class(BoostPost, x), from_none], self.rewind)
        if self.boost is not None:
            result["boost"] = from_union([lambda x: to_class(Boost, x), from_none], self.boost)
        if self.boost_post is not None:
            result["boostPost"] = from_union([lambda x: to_class(BoostPost, x), from_none], self.boost_post)
        if self.level_up is not None:
            result["levelUp"] = from_union([lambda x: to_class(Boost, x), from_none], self.level_up)
        if self.view_last_seen is not None:
            result["viewLastSeen"] = from_union([lambda x: to_class(BoostPost, x), from_none], self.view_last_seen)
        if self.sticker_pack is not None:
            result["stickerPack"] = from_union([lambda x: to_class(BoostPost, x), from_none], self.sticker_pack)
        if self.reactivate_chat is not None:
            result["reactivateChat"] = from_union([lambda x: to_class(BoostPost, x), from_none], self.reactivate_chat)
        if self.gifts is not None:
            result["gifts"] = from_union([lambda x: from_list(lambda y: to_class(Gift, y), x), from_none], self.gifts)
        if self.awards is not None:
            result["awards"] = from_union([lambda x: from_list(lambda y: to_class(Award, y), x), from_none],
                                          self.awards)
        return result


class Category(Enum):
    ACTIVITIES = "Activities"
    ASTROLOGY = "Astrology"
    CAUSES = "Causes"
    CREATIVITY = "Creativity"
    ENNEAGRAM = "Enneagram"
    FILM_LITERATURE = "Film & Literature"
    FOOD_DRINK = "Food & Drink"
    GAMES = "Games"
    MBTI = "MBTI"
    MUSIC = "Music"
    PETS = "Pets"
    SPORTS = "Sports"
    TOPICS = "Topics"


@dataclasses.dataclass
class InitAppResponseInterest:
    category: Optional[Category] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InitAppResponseInterest':
        assert isinstance(obj, dict)
        category = from_union([Category, from_none], obj.get("category"))
        name = from_union([from_str, from_none], obj.get("name"))
        return InitAppResponseInterest(category, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.category is not None:
            result["category"] = from_union([lambda x: to_enum(Category, x), from_none], self.category)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclasses.dataclass
class PurchaseInfo:
    status: Optional[str] = None
    product_id: Optional[str] = None
    expiration_date: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurchaseInfo':
        assert isinstance(obj, dict)
        status = from_union([from_str, from_none], obj.get("status"))
        product_id = from_union([from_str, from_none], obj.get("productId"))
        expiration_date = from_union([from_datetime, from_none], obj.get("expirationDate"))
        return PurchaseInfo(status, product_id, expiration_date)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.status is not None:
            result["status"] = from_union([from_str, from_none], self.status)
        if self.product_id is not None:
            result["productId"] = from_union([from_str, from_none], self.product_id)
        if self.expiration_date is not None:
            result["expirationDate"] = from_union([lambda x: x.isoformat(), from_none], self.expiration_date)
        return result


@dataclasses.dataclass
class LocationComponents:
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LocationComponents':
        assert isinstance(obj, dict)
        city = from_union([from_str, from_none], obj.get("city"))
        state = from_union([from_str, from_none], obj.get("state"))
        country = from_union([from_str, from_none], obj.get("country"))
        return LocationComponents(city, state, country)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.city is not None:
            result["city"] = from_union([from_str, from_none], self.city)
        if self.state is not None:
            result["state"] = from_union([from_str, from_none], self.state)
        if self.country is not None:
            result["country"] = from_union([from_str, from_none], self.country)
        return result


@dataclasses.dataclass
class AISettings:
    output_language: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AISettings':
        assert isinstance(obj, dict)
        output_language = from_union([from_str, from_none], obj.get("outputLanguage"))
        return AISettings(output_language)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.output_language is not None:
            result["outputLanguage"] = from_union([from_str, from_none], self.output_language)
        return result


@dataclasses.dataclass
class IncomingRequestsPreferences:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'IncomingRequestsPreferences':
        assert isinstance(obj, dict)
        return IncomingRequestsPreferences()

    def to_dict(self) -> dict:
        return self.__dict__


@dataclasses.dataclass
class UserInterest:
    id: Optional[str] = None
    category: Optional[Category] = None
    interest: Optional[str] = None
    name: Optional[str] = None
    allow_images: Optional[bool] = None
    num_followers: Optional[int] = None
    num_questions: Optional[int] = None
    num_questions_per_language: Optional[Dict[str, int]] = None
    similar: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserInterest':
        assert isinstance(obj, dict)
        _id = from_union([from_str, from_none], obj.get("_id"))
        category = from_union([Category, from_none], obj.get("category"))
        interest = from_union([from_str, from_none], obj.get("interest"))
        name = from_union([from_str, from_none], obj.get("name"))
        allow_images = from_union([from_bool, from_none], obj.get("allowImages"))
        num_followers = from_union([from_int, from_none], obj.get("numFollowers"))
        num_questions = from_union([from_int, from_none], obj.get("numQuestions"))
        num_questions_per_language = from_union([lambda x: from_dict(from_int, x), from_none],
                                                obj.get("numQuestionsPerLanguage"))
        similar = from_union([lambda x: from_list(from_str, x), from_none], obj.get("similar"))
        return UserInterest(_id, category, interest, name, allow_images, num_followers, num_questions,
                            num_questions_per_language, similar)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["_id"] = from_union([from_str, from_none], self.id)
        if self.category is not None:
            result["category"] = from_union([lambda x: to_enum(Category, x), from_none], self.category)
        if self.interest is not None:
            result["interest"] = from_union([from_str, from_none], self.interest)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.allow_images is not None:
            result["allowImages"] = from_union([from_bool, from_none], self.allow_images)
        if self.num_followers is not None:
            result["numFollowers"] = from_union([from_int, from_none], self.num_followers)
        if self.num_questions is not None:
            result["numQuestions"] = from_union([from_int, from_none], self.num_questions)
        if self.num_questions_per_language is not None:
            result["numQuestionsPerLanguage"] = from_union([lambda x: from_dict(from_int, x), from_none],
                                                           self.num_questions_per_language)
        if self.similar is not None:
            result["similar"] = from_union([lambda x: from_list(from_str, x), from_none], self.similar)
        return result


@dataclasses.dataclass
class MoreAboutUser:
    exercise: Optional[str] = None
    education_level: Optional[str] = None
    drinking: Optional[str] = None
    smoking: Optional[str] = None
    kids: Optional[str] = None
    religion: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MoreAboutUser':
        assert isinstance(obj, dict)
        exercise = from_union([from_str, from_none], obj.get("exercise"))
        education_level = from_union([from_str, from_none], obj.get("educationLevel"))
        drinking = from_union([from_str, from_none], obj.get("drinking"))
        smoking = from_union([from_str, from_none], obj.get("smoking"))
        kids = from_union([from_str, from_none], obj.get("kids"))
        religion = from_union([from_str, from_none], obj.get("religion"))
        return MoreAboutUser(exercise, education_level, drinking, smoking, kids, religion)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.exercise is not None:
            result["exercise"] = from_union([from_str, from_none], self.exercise)
        if self.education_level is not None:
            result["educationLevel"] = from_union([from_str, from_none], self.education_level)
        if self.drinking is not None:
            result["drinking"] = from_union([from_str, from_none], self.drinking)
        if self.smoking is not None:
            result["smoking"] = from_union([from_str, from_none], self.smoking)
        if self.kids is not None:
            result["kids"] = from_union([from_str, from_none], self.kids)
        if self.religion is not None:
            result["religion"] = from_union([from_str, from_none], self.religion)
        return result


@dataclasses.dataclass
class Personality:
    mbti: Optional[str] = None
    avatar: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Personality':
        assert isinstance(obj, dict)
        mbti = from_union([from_str, from_none], obj.get("mbti"))
        avatar = from_union([from_str, from_none], obj.get("avatar"))
        return Personality(mbti, avatar)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.mbti is not None:
            result["mbti"] = from_union([from_str, from_none], self.mbti)
        if self.avatar is not None:
            result["avatar"] = from_union([from_str, from_none], self.avatar)
        return result


@dataclasses.dataclass
class Preferences:
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    personality: Optional[List[str]] = None
    dating: Optional[List[str]] = None
    friends: Optional[List[str]] = None
    show_verified_only: Optional[bool] = None
    distance: Any = None
    keywords: Optional[List[Any]] = None
    preferences_global: Optional[bool] = None
    local: Optional[bool] = None
    bio_length: Any = None
    distance2: Any = None
    max_height: Any = None
    min_height: Any = None
    same_country_only: Optional[bool] = None
    show_to_verified_only: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Preferences':
        assert isinstance(obj, dict)
        min_age = from_union([from_int, from_none], obj.get("minAge"))
        max_age = from_union([from_int, from_none], obj.get("maxAge"))
        personality = from_union([lambda x: from_list(from_str, x), from_none], obj.get("personality"))
        dating = from_union([lambda x: from_list(from_str, x), from_none], obj.get("dating"))
        friends = from_union([lambda x: from_list(from_str, x), from_none], obj.get("friends"))
        show_verified_only = from_union([from_bool, from_none], obj.get("showVerifiedOnly"))
        distance = from_none(obj.get("distance"))
        keywords = from_union([lambda x: from_list(lambda y: y, x), from_none], obj.get("keywords"))
        preferences_global = from_union([from_bool, from_none], obj.get("global"))
        local = from_union([from_bool, from_none], obj.get("local"))
        bio_length = from_none(obj.get("bioLength"))
        distance2 = from_none(obj.get("distance2"))
        max_height = from_none(obj.get("maxHeight"))
        min_height = from_none(obj.get("minHeight"))
        same_country_only = from_union([from_bool, from_none], obj.get("sameCountryOnly"))
        show_to_verified_only = from_union([from_bool, from_none], obj.get("showToVerifiedOnly"))
        return Preferences(min_age, max_age, personality, dating, friends, show_verified_only, distance, keywords,
                           preferences_global, local, bio_length, distance2, max_height, min_height, same_country_only,
                           show_to_verified_only)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.min_age is not None:
            result["minAge"] = from_union([from_int, from_none], self.min_age)
        if self.max_age is not None:
            result["maxAge"] = from_union([from_int, from_none], self.max_age)
        if self.personality is not None:
            result["personality"] = from_union([lambda x: from_list(from_str, x), from_none], self.personality)
        if self.dating is not None:
            result["dating"] = from_union([lambda x: from_list(from_str, x), from_none], self.dating)
        if self.friends is not None:
            result["friends"] = from_union([lambda x: from_list(from_str, x), from_none], self.friends)
        if self.show_verified_only is not None:
            result["showVerifiedOnly"] = from_union([from_bool, from_none], self.show_verified_only)
        if self.distance is not None:
            result["distance"] = from_none(self.distance)
        if self.keywords is not None:
            result["keywords"] = from_union([lambda x: from_list(lambda y: y, x), from_none], self.keywords)
        if self.preferences_global is not None:
            result["global"] = from_union([from_bool, from_none], self.preferences_global)
        if self.local is not None:
            result["local"] = from_union([from_bool, from_none], self.local)
        if self.bio_length is not None:
            result["bioLength"] = from_none(self.bio_length)
        if self.distance2 is not None:
            result["distance2"] = from_none(self.distance2)
        if self.max_height is not None:
            result["maxHeight"] = from_none(self.max_height)
        if self.min_height is not None:
            result["minHeight"] = from_none(self.min_height)
        if self.same_country_only is not None:
            result["sameCountryOnly"] = from_union([from_bool, from_none], self.same_country_only)
        if self.show_to_verified_only is not None:
            result["showToVerifiedOnly"] = from_union([from_bool, from_none], self.show_to_verified_only)
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


@dataclasses.dataclass
class WingmanSettings:
    warnings: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'WingmanSettings':
        assert isinstance(obj, dict)
        warnings = from_union([from_bool, from_none], obj.get("warnings"))
        return WingmanSettings(warnings)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.warnings is not None:
            result["warnings"] = from_union([from_bool, from_none], self.warnings)
        return result


@dataclasses.dataclass
class User:
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    first_name: Optional[str] = None
    birthday: Optional[datetime] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    height: Optional[int] = None
    ethnicities: Optional[List[str]] = None
    horoscope: Optional[str] = None
    description: Optional[str] = None
    preferences: Optional[Preferences] = None
    incoming_requests_preferences: Optional[IncomingRequestsPreferences] = None
    custom_feeds: Optional[List[Any]] = None
    pictures: Optional[List[str]] = None
    personality: Optional[Personality] = None
    education: Optional[str] = None
    teleport: Optional[bool] = None
    actual_location: Optional[str] = None
    location: Optional[str] = None
    location_components: Optional[LocationComponents] = None
    actual_location_components: Optional[LocationComponents] = None
    prompts: Optional[List[Prompt]] = None
    crown: Optional[bool] = None
    handle: Optional[str] = None
    searchable: Optional[bool] = None
    hidden: Optional[bool] = None
    hide_city: Optional[bool] = None
    hide_read_receipts: Optional[bool] = None
    hide_questions: Optional[bool] = None
    hide_comments: Optional[bool] = None
    hide_horoscope: Optional[bool] = None
    hidden_contacts: Optional[bool] = None
    more_about_user: Optional[MoreAboutUser] = None
    dark_mode: Optional[bool] = None
    use_metric_system: Optional[bool] = None
    instant_match: Optional[bool] = None
    premium: Optional[bool] = None
    premium_v2: Optional[bool] = None
    god_mode: Optional[bool] = None
    product_id_purchased: Optional[str] = None
    coins: Optional[int] = None
    interplanetary_mode: Optional[bool] = None
    show_free_trial_option: Optional[bool] = None
    push_notification_settings: Optional[Dict[str, bool]] = None
    wingman_settings: Optional[WingmanSettings] = None
    interests: Optional[List[UserInterest]] = None
    interest_names: Optional[List[str]] = None
    hidden_interests: Optional[List[Any]] = None
    karma: Optional[int] = None
    approve_all_followers: Optional[bool] = None
    auto_follow_likes: Optional[bool] = None
    auto_follow_matches: Optional[bool] = None
    num_followers: Optional[int] = None
    num_following: Optional[int] = None
    num_follow_requests: Optional[int] = None
    num_profile_views: Optional[int] = None
    num_pending_likes: Optional[int] = None
    verified: Optional[bool] = None
    verification_status: Optional[str] = None
    languages: Optional[List[str]] = None
    sticker_pack_purchases: Optional[List[Any]] = None
    num_super_likes: Optional[int] = None
    num_boo_ai_neurons: Optional[int] = None
    num_db_uploads: Optional[int] = None
    db_upload_coins_received: Optional[int] = None
    db_upload_karma_received: Optional[int] = None
    rejection_reason: Optional[str] = None
    autoplay: Optional[bool] = None
    hide_from_keywords: Optional[List[Any]] = None
    ai_settings: Optional[AISettings] = None
    interest_points: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        _id = from_union([from_str, from_none], obj.get("_id"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        first_name = from_union([from_str, from_none], obj.get("firstName"))
        birthday = from_union([from_datetime, from_none], obj.get("birthday"))
        gender = from_union([from_str, from_none], obj.get("gender"))
        age = from_union([from_int, from_none], obj.get("age"))
        height = from_union([from_int, from_none], obj.get("height"))
        ethnicities = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ethnicities"))
        horoscope = from_union([from_str, from_none], obj.get("horoscope"))
        description = from_union([from_str, from_none], obj.get("description"))
        preferences = from_union([Preferences.from_dict, from_none], obj.get("preferences"))
        incoming_requests_preferences = from_union([IncomingRequestsPreferences.from_dict, from_none],
                                                   obj.get("incomingRequestsPreferences"))
        custom_feeds = from_union([lambda x: from_list(lambda y: y, x), from_none], obj.get("customFeeds"))
        pictures = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pictures"))
        personality = from_union([Personality.from_dict, from_none], obj.get("personality"))
        education = from_union([from_str, from_none], obj.get("education"))
        teleport = from_union([from_bool, from_none], obj.get("teleport"))
        actual_location = from_union([from_str, from_none], obj.get("actualLocation"))
        location = from_union([from_str, from_none], obj.get("location"))
        location_components = from_union([LocationComponents.from_dict, from_none], obj.get("locationComponents"))
        actual_location_components = from_union([LocationComponents.from_dict, from_none],
                                                obj.get("actualLocationComponents"))
        prompts = from_union([lambda x: from_list(Prompt.from_dict, x), from_none], obj.get("prompts"))
        crown = from_union([from_bool, from_none], obj.get("crown"))
        handle = from_union([from_str, from_none], obj.get("handle"))
        searchable = from_union([from_bool, from_none], obj.get("searchable"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        hide_city = from_union([from_bool, from_none], obj.get("hideCity"))
        hide_read_receipts = from_union([from_bool, from_none], obj.get("hideReadReceipts"))
        hide_questions = from_union([from_bool, from_none], obj.get("hideQuestions"))
        hide_comments = from_union([from_bool, from_none], obj.get("hideComments"))
        hide_horoscope = from_union([from_bool, from_none], obj.get("hideHoroscope"))
        hidden_contacts = from_union([from_bool, from_none], obj.get("hiddenContacts"))
        more_about_user = from_union([MoreAboutUser.from_dict, from_none], obj.get("moreAboutUser"))
        dark_mode = from_union([from_bool, from_none], obj.get("darkMode"))
        use_metric_system = from_union([from_bool, from_none], obj.get("useMetricSystem"))
        instant_match = from_union([from_bool, from_none], obj.get("instantMatch"))
        premium = from_union([from_bool, from_none], obj.get("premium"))
        premium_v2 = from_union([from_bool, from_none], obj.get("premiumV2"))
        god_mode = from_union([from_bool, from_none], obj.get("godMode"))
        product_id_purchased = from_union([from_str, from_none], obj.get("productIdPurchased"))
        coins = from_union([from_int, from_none], obj.get("coins"))
        interplanetary_mode = from_union([from_bool, from_none], obj.get("interplanetaryMode"))
        show_free_trial_option = from_union([from_bool, from_none], obj.get("showFreeTrialOption"))
        push_notification_settings = from_union([lambda x: from_dict(from_bool, x), from_none],
                                                obj.get("pushNotificationSettings"))
        wingman_settings = from_union([WingmanSettings.from_dict, from_none], obj.get("wingmanSettings"))
        interests = from_union([lambda x: from_list(UserInterest.from_dict, x), from_none], obj.get("interests"))
        interest_names = from_union([lambda x: from_list(from_str, x), from_none], obj.get("interestNames"))
        hidden_interests = from_union([lambda x: from_list(lambda y: y, x), from_none], obj.get("hiddenInterests"))
        karma = from_union([from_int, from_none], obj.get("karma"))
        approve_all_followers = from_union([from_bool, from_none], obj.get("approveAllFollowers"))
        auto_follow_likes = from_union([from_bool, from_none], obj.get("autoFollowLikes"))
        auto_follow_matches = from_union([from_bool, from_none], obj.get("autoFollowMatches"))
        num_followers = from_union([from_int, from_none], obj.get("numFollowers"))
        num_following = from_union([from_int, from_none], obj.get("numFollowing"))
        num_follow_requests = from_union([from_int, from_none], obj.get("numFollowRequests"))
        num_profile_views = from_union([from_int, from_none], obj.get("numProfileViews"))
        num_pending_likes = from_union([from_int, from_none], obj.get("numPendingLikes"))
        verified = from_union([from_bool, from_none], obj.get("verified"))
        verification_status = from_union([from_str, from_none], obj.get("verificationStatus"))
        languages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("languages"))
        sticker_pack_purchases = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                            obj.get("stickerPackPurchases"))
        num_super_likes = from_union([from_int, from_none], obj.get("numSuperLikes"))
        num_boo_ai_neurons = from_union([from_int, from_none], obj.get("numBooAINeurons"))
        num_db_uploads = from_union([from_int, from_none], obj.get("numDbUploads"))
        db_upload_coins_received = from_union([from_int, from_none], obj.get("dbUploadCoinsReceived"))
        db_upload_karma_received = from_union([from_int, from_none], obj.get("dbUploadKarmaReceived"))
        rejection_reason = from_union([from_str, from_none], obj.get("rejectionReason"))
        autoplay = from_union([from_bool, from_none], obj.get("autoplay"))
        hide_from_keywords = from_union([lambda x: from_list(lambda y: y, x), from_none], obj.get("hideFromKeywords"))
        ai_settings = from_union([AISettings.from_dict, from_none], obj.get("aiSettings"))
        interest_points = from_union([lambda x: from_list(lambda y: y, x), from_none], obj.get("interestPoints"))
        return User(_id, created_at, first_name, birthday, gender, age, height, ethnicities, horoscope, description,
                    preferences, incoming_requests_preferences, custom_feeds, pictures, personality, education,
                    teleport, actual_location, location, location_components, actual_location_components, prompts,
                    crown, handle, searchable, hidden, hide_city, hide_read_receipts, hide_questions, hide_comments,
                    hide_horoscope, hidden_contacts, more_about_user, dark_mode, use_metric_system, instant_match,
                    premium, premium_v2, god_mode, product_id_purchased, coins, interplanetary_mode,
                    show_free_trial_option, push_notification_settings, wingman_settings, interests, interest_names,
                    hidden_interests, karma, approve_all_followers, auto_follow_likes, auto_follow_matches,
                    num_followers, num_following, num_follow_requests, num_profile_views, num_pending_likes, verified,
                    verification_status, languages, sticker_pack_purchases, num_super_likes, num_boo_ai_neurons,
                    num_db_uploads, db_upload_coins_received, db_upload_karma_received, rejection_reason, autoplay,
                    hide_from_keywords, ai_settings, interest_points)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["_id"] = from_union([from_str, from_none], self.id)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.first_name is not None:
            result["firstName"] = from_union([from_str, from_none], self.first_name)
        if self.birthday is not None:
            result["birthday"] = from_union([lambda x: x.isoformat(), from_none], self.birthday)
        if self.gender is not None:
            result["gender"] = from_union([from_str, from_none], self.gender)
        if self.age is not None:
            result["age"] = from_union([from_int, from_none], self.age)
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        if self.ethnicities is not None:
            result["ethnicities"] = from_union([lambda x: from_list(from_str, x), from_none], self.ethnicities)
        if self.horoscope is not None:
            result["horoscope"] = from_union([from_str, from_none], self.horoscope)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.preferences is not None:
            result["preferences"] = from_union([lambda x: to_class(Preferences, x), from_none], self.preferences)
        if self.incoming_requests_preferences is not None:
            result["incomingRequestsPreferences"] = from_union(
                [lambda x: to_class(IncomingRequestsPreferences, x), from_none], self.incoming_requests_preferences)
        if self.custom_feeds is not None:
            result["customFeeds"] = from_union([lambda x: from_list(lambda y: y, x), from_none], self.custom_feeds)
        if self.pictures is not None:
            result["pictures"] = from_union([lambda x: from_list(from_str, x), from_none], self.pictures)
        if self.personality is not None:
            result["personality"] = from_union([lambda x: to_class(Personality, x), from_none], self.personality)
        if self.education is not None:
            result["education"] = from_union([from_str, from_none], self.education)
        if self.teleport is not None:
            result["teleport"] = from_union([from_bool, from_none], self.teleport)
        if self.actual_location is not None:
            result["actualLocation"] = from_union([from_str, from_none], self.actual_location)
        if self.location is not None:
            result["location"] = from_union([from_str, from_none], self.location)
        if self.location_components is not None:
            result["locationComponents"] = from_union([lambda x: to_class(LocationComponents, x), from_none],
                                                      self.location_components)
        if self.actual_location_components is not None:
            result["actualLocationComponents"] = from_union([lambda x: to_class(LocationComponents, x), from_none],
                                                            self.actual_location_components)
        if self.prompts is not None:
            result["prompts"] = from_union([lambda x: from_list(lambda y: to_class(Prompt, y), x), from_none],
                                           self.prompts)
        if self.crown is not None:
            result["crown"] = from_union([from_bool, from_none], self.crown)
        if self.handle is not None:
            result["handle"] = from_union([from_str, from_none], self.handle)
        if self.searchable is not None:
            result["searchable"] = from_union([from_bool, from_none], self.searchable)
        if self.hidden is not None:
            result["hidden"] = from_union([from_bool, from_none], self.hidden)
        if self.hide_city is not None:
            result["hideCity"] = from_union([from_bool, from_none], self.hide_city)
        if self.hide_read_receipts is not None:
            result["hideReadReceipts"] = from_union([from_bool, from_none], self.hide_read_receipts)
        if self.hide_questions is not None:
            result["hideQuestions"] = from_union([from_bool, from_none], self.hide_questions)
        if self.hide_comments is not None:
            result["hideComments"] = from_union([from_bool, from_none], self.hide_comments)
        if self.hide_horoscope is not None:
            result["hideHoroscope"] = from_union([from_bool, from_none], self.hide_horoscope)
        if self.hidden_contacts is not None:
            result["hiddenContacts"] = from_union([from_bool, from_none], self.hidden_contacts)
        if self.more_about_user is not None:
            result["moreAboutUser"] = from_union([lambda x: to_class(MoreAboutUser, x), from_none],
                                                 self.more_about_user)
        if self.dark_mode is not None:
            result["darkMode"] = from_union([from_bool, from_none], self.dark_mode)
        if self.use_metric_system is not None:
            result["useMetricSystem"] = from_union([from_bool, from_none], self.use_metric_system)
        if self.instant_match is not None:
            result["instantMatch"] = from_union([from_bool, from_none], self.instant_match)
        if self.premium is not None:
            result["premium"] = from_union([from_bool, from_none], self.premium)
        if self.premium_v2 is not None:
            result["premiumV2"] = from_union([from_bool, from_none], self.premium_v2)
        if self.god_mode is not None:
            result["godMode"] = from_union([from_bool, from_none], self.god_mode)
        if self.product_id_purchased is not None:
            result["productIdPurchased"] = from_union([from_str, from_none], self.product_id_purchased)
        if self.coins is not None:
            result["coins"] = from_union([from_int, from_none], self.coins)
        if self.interplanetary_mode is not None:
            result["interplanetaryMode"] = from_union([from_bool, from_none], self.interplanetary_mode)
        if self.show_free_trial_option is not None:
            result["showFreeTrialOption"] = from_union([from_bool, from_none], self.show_free_trial_option)
        if self.push_notification_settings is not None:
            result["pushNotificationSettings"] = from_union([lambda x: from_dict(from_bool, x), from_none],
                                                            self.push_notification_settings)
        if self.wingman_settings is not None:
            result["wingmanSettings"] = from_union([lambda x: to_class(WingmanSettings, x), from_none],
                                                   self.wingman_settings)
        if self.interests is not None:
            result["interests"] = from_union([lambda x: from_list(lambda y: to_class(UserInterest, y), x), from_none],
                                             self.interests)
        if self.interest_names is not None:
            result["interestNames"] = from_union([lambda x: from_list(from_str, x), from_none], self.interest_names)
        if self.hidden_interests is not None:
            result["hiddenInterests"] = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                                   self.hidden_interests)
        if self.karma is not None:
            result["karma"] = from_union([from_int, from_none], self.karma)
        if self.approve_all_followers is not None:
            result["approveAllFollowers"] = from_union([from_bool, from_none], self.approve_all_followers)
        if self.auto_follow_likes is not None:
            result["autoFollowLikes"] = from_union([from_bool, from_none], self.auto_follow_likes)
        if self.auto_follow_matches is not None:
            result["autoFollowMatches"] = from_union([from_bool, from_none], self.auto_follow_matches)
        if self.num_followers is not None:
            result["numFollowers"] = from_union([from_int, from_none], self.num_followers)
        if self.num_following is not None:
            result["numFollowing"] = from_union([from_int, from_none], self.num_following)
        if self.num_follow_requests is not None:
            result["numFollowRequests"] = from_union([from_int, from_none], self.num_follow_requests)
        if self.num_profile_views is not None:
            result["numProfileViews"] = from_union([from_int, from_none], self.num_profile_views)
        if self.num_pending_likes is not None:
            result["numPendingLikes"] = from_union([from_int, from_none], self.num_pending_likes)
        if self.verified is not None:
            result["verified"] = from_union([from_bool, from_none], self.verified)
        if self.verification_status is not None:
            result["verificationStatus"] = from_union([from_str, from_none], self.verification_status)
        if self.languages is not None:
            result["languages"] = from_union([lambda x: from_list(from_str, x), from_none], self.languages)
        if self.sticker_pack_purchases is not None:
            result["stickerPackPurchases"] = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                                        self.sticker_pack_purchases)
        if self.num_super_likes is not None:
            result["numSuperLikes"] = from_union([from_int, from_none], self.num_super_likes)
        if self.num_boo_ai_neurons is not None:
            result["numBooAINeurons"] = from_union([from_int, from_none], self.num_boo_ai_neurons)
        if self.num_db_uploads is not None:
            result["numDbUploads"] = from_union([from_int, from_none], self.num_db_uploads)
        if self.db_upload_coins_received is not None:
            result["dbUploadCoinsReceived"] = from_union([from_int, from_none], self.db_upload_coins_received)
        if self.db_upload_karma_received is not None:
            result["dbUploadKarmaReceived"] = from_union([from_int, from_none], self.db_upload_karma_received)
        if self.rejection_reason is not None:
            result["rejectionReason"] = from_union([from_str, from_none], self.rejection_reason)
        if self.autoplay is not None:
            result["autoplay"] = from_union([from_bool, from_none], self.autoplay)
        if self.hide_from_keywords is not None:
            result["hideFromKeywords"] = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                                    self.hide_from_keywords)
        if self.ai_settings is not None:
            result["aiSettings"] = from_union([lambda x: to_class(AISettings, x), from_none], self.ai_settings)
        if self.interest_points is not None:
            result["interestPoints"] = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                                  self.interest_points)
        return result


@dataclasses.dataclass
class InitAppResponse:
    user: Optional[User] = None
    coin_products: Optional[CoinProducts] = None
    interests: Optional[List[InitAppResponseInterest]] = None
    num_pending_chats: Optional[int] = None
    karma_tiers: Optional[List[int]] = None
    karma_tier_coin_rewards: Optional[List[int]] = None
    karma_tier_swipe_limits: Optional[List[int]] = None
    next_login_reward: Optional[datetime] = None
    free_swipe_from_qod_received: Optional[bool] = None
    free_swipe_received_for_qods: Optional[List[Any]] = None
    karma_change: Optional[int] = None
    purchase_info: Optional[PurchaseInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InitAppResponse':
        assert isinstance(obj, dict)
        user = from_union([User.from_dict, from_none], obj.get("user"))
        coin_products = from_union([CoinProducts.from_dict, from_none], obj.get("coinProducts"))
        interests = from_union([lambda x: from_list(InitAppResponseInterest.from_dict, x), from_none],
                               obj.get("interests"))
        num_pending_chats = from_union([from_int, from_none], obj.get("numPendingChats"))
        karma_tiers = from_union([lambda x: from_list(from_int, x), from_none], obj.get("karmaTiers"))
        karma_tier_coin_rewards = from_union([lambda x: from_list(from_int, x), from_none],
                                             obj.get("karmaTierCoinRewards"))
        karma_tier_swipe_limits = from_union([lambda x: from_list(from_int, x), from_none],
                                             obj.get("karmaTierSwipeLimits"))
        next_login_reward = from_union([from_datetime, from_none], obj.get("nextLoginReward"))
        free_swipe_from_qod_received = from_union([from_bool, from_none], obj.get("freeSwipeFromQodReceived"))
        free_swipe_received_for_qods = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                                  obj.get("freeSwipeReceivedForQods"))
        karma_change = from_union([from_int, from_none], obj.get("karmaChange"))
        purchase_info = from_union([PurchaseInfo.from_dict, from_none], obj.get("purchaseInfo"))
        return InitAppResponse(user, coin_products, interests, num_pending_chats, karma_tiers, karma_tier_coin_rewards,
                               karma_tier_swipe_limits, next_login_reward, free_swipe_from_qod_received,
                               free_swipe_received_for_qods, karma_change, purchase_info)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.user is not None:
            result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        if self.coin_products is not None:
            result["coinProducts"] = from_union([lambda x: to_class(CoinProducts, x), from_none], self.coin_products)
        if self.interests is not None:
            result["interests"] = from_union(
                [lambda x: from_list(lambda y: to_class(InitAppResponseInterest, y), x), from_none], self.interests)
        if self.num_pending_chats is not None:
            result["numPendingChats"] = from_union([from_int, from_none], self.num_pending_chats)
        if self.karma_tiers is not None:
            result["karmaTiers"] = from_union([lambda x: from_list(from_int, x), from_none], self.karma_tiers)
        if self.karma_tier_coin_rewards is not None:
            result["karmaTierCoinRewards"] = from_union([lambda x: from_list(from_int, x), from_none],
                                                        self.karma_tier_coin_rewards)
        if self.karma_tier_swipe_limits is not None:
            result["karmaTierSwipeLimits"] = from_union([lambda x: from_list(from_int, x), from_none],
                                                        self.karma_tier_swipe_limits)
        if self.next_login_reward is not None:
            result["nextLoginReward"] = from_union([lambda x: x.isoformat(), from_none], self.next_login_reward)
        if self.free_swipe_from_qod_received is not None:
            result["freeSwipeFromQodReceived"] = from_union([from_bool, from_none], self.free_swipe_from_qod_received)
        if self.free_swipe_received_for_qods is not None:
            result["freeSwipeReceivedForQods"] = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                                            self.free_swipe_received_for_qods)
        if self.karma_change is not None:
            result["karmaChange"] = from_union([from_int, from_none], self.karma_change)
        if self.purchase_info is not None:
            result["purchaseInfo"] = from_union([lambda x: to_class(PurchaseInfo, x), from_none], self.purchase_info)
        return result


def init_app_response_from_dict(s: Any) -> InitAppResponse:
    return InitAppResponse.from_dict(s)


def init_app_response_to_dict(x: InitAppResponse) -> Any:
    return to_class(InitAppResponse, x)
