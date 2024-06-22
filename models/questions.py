import dataclasses
from datetime import datetime
from typing import Optional, List, Any

from models.awards import Award
from models.interest import Interest
from models.utils import from_union, from_list, to_class, from_none, from_str, from_int, from_bool, to_float, \
    from_float, from_datetime


@dataclasses.dataclass
class Personality:
    mbti: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Personality':
        assert isinstance(obj, dict)
        mbti = from_union([from_str, from_none], obj.get("mbti"))
        return Personality(mbti)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.mbti is not None:
            result["mbti"] = from_union([from_str, from_none], self.mbti)
        return result


@dataclasses.dataclass
class ProfilePreview:
    id: Optional[str] = None
    first_name: Optional[str] = None
    picture: Optional[str] = None
    personality: Optional[Personality] = None
    enneagram: Optional[str] = None
    horoscope: Optional[str] = None
    karma: Optional[float] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    handle: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ProfilePreview':
        assert isinstance(obj, dict)
        _id = from_union([from_str, from_none], obj.get("_id"))
        first_name = from_union([from_str, from_none], obj.get("firstName"))
        picture = from_union([from_str, from_none], obj.get("picture"))
        personality = from_union([Personality.from_dict, from_none], obj.get("personality"))
        enneagram = from_union([from_str, from_none], obj.get("enneagram"))
        horoscope = from_union([from_str, from_none], obj.get("horoscope"))
        karma = from_union([from_float, from_none], obj.get("karma"))
        gender = from_union([from_str, from_none], obj.get("gender"))
        age = from_union([from_int, from_none], obj.get("age"))
        handle = from_union([from_str, from_none], obj.get("handle"))
        return ProfilePreview(_id, first_name, picture, personality, enneagram, horoscope, karma, gender, age, handle)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["_id"] = from_union([from_str, from_none], self.id)
        if self.first_name is not None:
            result["firstName"] = from_union([from_str, from_none], self.first_name)
        if self.picture is not None:
            result["picture"] = from_union([from_str, from_none], self.picture)
        if self.personality is not None:
            result["personality"] = from_union([lambda x: to_class(Personality, x), from_none], self.personality)
        if self.enneagram is not None:
            result["enneagram"] = from_union([from_str, from_none], self.enneagram)
        if self.horoscope is not None:
            result["horoscope"] = from_union([from_str, from_none], self.horoscope)
        if self.karma is not None:
            result["karma"] = from_union([to_float, from_none], self.karma)
        if self.gender is not None:
            result["gender"] = from_union([from_str, from_none], self.gender)
        if self.age is not None:
            result["age"] = from_union([from_int, from_none], self.age)
        if self.handle is not None:
            result["handle"] = from_union([from_str, from_none], self.handle)
        return result


@dataclasses.dataclass
class Question:
    id: Optional[str] = None
    web_id: Optional[str] = None
    created_at: Optional[datetime] = None
    profile_preview: Optional[ProfilePreview] = None
    allow_incoming_requests: Optional[bool] = None
    title: Optional[str] = None
    text: Optional[str] = None
    image: Optional[str] = None
    video_thumbnail: Optional[str] = None
    aspect_ratio: Optional[float] = None
    interest: Optional[Interest] = None
    interest_name: Optional[str] = None
    num_comments: Optional[int] = None
    num_likes: Optional[int] = None
    num_views: Optional[int] = None
    is_deleted: Optional[bool] = None
    is_edited: Optional[bool] = None
    has_user_liked: Optional[bool] = None
    has_user_saved: Optional[bool] = None
    language: Optional[str] = None
    url: Optional[str] = None
    awards: Optional[Award] = None
    friends_that_commented: Optional[List[Any]] = None
    is_boosted: Optional[bool] = None
    created_by_interest_rank: Optional[int] = None
    linked_keywords: Optional[List[Any]] = None
    linked_explore_keywords: Optional[List[str]] = None
    linked_pillar_keywords: Optional[List[Any]] = None
    linked_categories: Optional[List[Any]] = None
    linked_subcategories: Optional[List[Any]] = None
    linked_profiles: Optional[List[Any]] = None
    mentioned_users_title: Optional[List[Any]] = None
    mentioned_users_text: Optional[List[Any]] = None
    hashtags: Optional[List[str]] = None
    alt_text: Optional[str] = None
    gif: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Question':
        assert isinstance(obj, dict)
        _id = from_union([from_str, from_none], obj.get("_id"))
        web_id = from_union([from_str, from_none], obj.get("webId"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        profile_preview = from_union([ProfilePreview.from_dict, from_none], obj.get("profilePreview"))
        allow_incoming_requests = from_union([from_bool, from_none], obj.get("allowIncomingRequests"))
        title = from_union([from_str, from_none], obj.get("title"))
        text = from_union([from_str, from_none], obj.get("text"))
        image = from_union([from_str, from_none], obj.get("image"))
        video_thumbnail = from_union([from_str, from_none], obj.get("videoThumbnail"))
        aspect_ratio = from_union([from_float, from_none], obj.get("aspectRatio"))
        interest = from_union([Interest.from_dict, from_none], obj.get("interest"))
        interest_name = from_union([from_str, from_none], obj.get("interestName"))
        num_comments = from_union([from_int, from_none], obj.get("numComments"))
        num_likes = from_union([from_int, from_none], obj.get("numLikes"))
        num_views = from_union([from_int, from_none], obj.get("numViews"))
        is_deleted = from_union([from_bool, from_none], obj.get("isDeleted"))
        is_edited = from_union([from_bool, from_none], obj.get("isEdited"))
        has_user_liked = from_union([from_bool, from_none], obj.get("hasUserLiked"))
        has_user_saved = from_union([from_bool, from_none], obj.get("hasUserSaved"))
        language = from_union([from_str, from_none], obj.get("language"))
        url = from_union([from_str, from_none], obj.get("url"))
        awards = from_union([Award.from_dict, from_none], obj.get("awards"))
        friends_that_commented = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                            obj.get("friendsThatCommented"))
        is_boosted = from_union([from_bool, from_none], obj.get("isBoosted"))
        created_by_interest_rank = from_union([from_int, from_none], obj.get("createdByInterestRank"))
        linked_keywords = from_union([lambda x: from_list(lambda y: y, x), from_none], obj.get("linkedKeywords"))
        linked_explore_keywords = from_union([lambda x: from_list(from_str, x), from_none],
                                             obj.get("linkedExploreKeywords"))
        linked_pillar_keywords = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                            obj.get("linkedPillarKeywords"))
        linked_categories = from_union([lambda x: from_list(lambda y: y, x), from_none], obj.get("linkedCategories"))
        linked_subcategories = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                          obj.get("linkedSubcategories"))
        linked_profiles = from_union([lambda x: from_list(lambda y: y, x), from_none], obj.get("linkedProfiles"))
        mentioned_users_title = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                           obj.get("mentionedUsersTitle"))
        mentioned_users_text = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                          obj.get("mentionedUsersText"))
        hashtags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("hashtags"))
        alt_text = from_union([from_str, from_none], obj.get("altText"))
        gif = from_union([from_str, from_none], obj.get("gif"))
        return Question(_id, web_id, created_at, profile_preview, allow_incoming_requests, title, text, image,
                        video_thumbnail, aspect_ratio, interest, interest_name, num_comments, num_likes, num_views,
                        is_deleted, is_edited, has_user_liked, has_user_saved, language, url, awards,
                        friends_that_commented, is_boosted, created_by_interest_rank, linked_keywords,
                        linked_explore_keywords, linked_pillar_keywords, linked_categories, linked_subcategories,
                        linked_profiles, mentioned_users_title, mentioned_users_text, hashtags, alt_text, gif)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["_id"] = from_union([from_str, from_none], self.id)
        if self.web_id is not None:
            result["webId"] = from_union([from_str, from_none], self.web_id)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.profile_preview is not None:
            result["profilePreview"] = from_union([lambda x: to_class(ProfilePreview, x), from_none],
                                                  self.profile_preview)
        if self.allow_incoming_requests is not None:
            result["allowIncomingRequests"] = from_union([from_bool, from_none], self.allow_incoming_requests)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.text is not None:
            result["text"] = from_union([from_str, from_none], self.text)
        if self.image is not None:
            result["image"] = from_union([from_str, from_none], self.image)
        if self.video_thumbnail is not None:
            result["videoThumbnail"] = from_union([from_str, from_none], self.video_thumbnail)
        if self.aspect_ratio is not None:
            result["aspectRatio"] = from_union([to_float, from_none], self.aspect_ratio)
        if self.interest is not None:
            result["interest"] = from_union([lambda x: to_class(Interest, x), from_none], self.interest)
        if self.interest_name is not None:
            result["interestName"] = from_union([from_str, from_none], self.interest_name)
        if self.num_comments is not None:
            result["numComments"] = from_union([from_int, from_none], self.num_comments)
        if self.num_likes is not None:
            result["numLikes"] = from_union([from_int, from_none], self.num_likes)
        if self.num_views is not None:
            result["numViews"] = from_union([from_int, from_none], self.num_views)
        if self.is_deleted is not None:
            result["isDeleted"] = from_union([from_bool, from_none], self.is_deleted)
        if self.is_edited is not None:
            result["isEdited"] = from_union([from_bool, from_none], self.is_edited)
        if self.has_user_liked is not None:
            result["hasUserLiked"] = from_union([from_bool, from_none], self.has_user_liked)
        if self.has_user_saved is not None:
            result["hasUserSaved"] = from_union([from_bool, from_none], self.has_user_saved)
        if self.language is not None:
            result["language"] = from_union([from_str, from_none], self.language)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.awards is not None:
            result["awards"] = from_union([lambda x: to_class(Award, x), from_none], self.awards)
        if self.friends_that_commented is not None:
            result["friendsThatCommented"] = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                                        self.friends_that_commented)
        if self.is_boosted is not None:
            result["isBoosted"] = from_union([from_bool, from_none], self.is_boosted)
        if self.created_by_interest_rank is not None:
            result["createdByInterestRank"] = from_union([from_int, from_none], self.created_by_interest_rank)
        if self.linked_keywords is not None:
            result["linkedKeywords"] = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                                  self.linked_keywords)
        if self.linked_explore_keywords is not None:
            result["linkedExploreKeywords"] = from_union([lambda x: from_list(from_str, x), from_none],
                                                         self.linked_explore_keywords)
        if self.linked_pillar_keywords is not None:
            result["linkedPillarKeywords"] = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                                        self.linked_pillar_keywords)
        if self.linked_categories is not None:
            result["linkedCategories"] = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                                    self.linked_categories)
        if self.linked_subcategories is not None:
            result["linkedSubcategories"] = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                                       self.linked_subcategories)
        if self.linked_profiles is not None:
            result["linkedProfiles"] = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                                  self.linked_profiles)
        if self.mentioned_users_title is not None:
            result["mentionedUsersTitle"] = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                                       self.mentioned_users_title)
        if self.mentioned_users_text is not None:
            result["mentionedUsersText"] = from_union([lambda x: from_list(lambda y: y, x), from_none],
                                                      self.mentioned_users_text)
        if self.hashtags is not None:
            result["hashtags"] = from_union([lambda x: from_list(from_str, x), from_none], self.hashtags)
        if self.alt_text is not None:
            result["altText"] = from_union([from_str, from_none], self.alt_text)
        if self.gif is not None:
            result["gif"] = from_none(self.gif)
        return result


@dataclasses.dataclass
class QuestionsResponse:
    questions: Optional[List[Question]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QuestionsResponse':
        assert isinstance(obj, dict)
        if obj.get('questions'):
            questions = from_list(Question.from_dict, obj.get('questions'))
        else:
            questions = None
        return QuestionsResponse(questions)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.questions is not None:
            result["questions"] = from_union([lambda x: from_list(lambda y: to_class(Question, y), x), from_none],
                                             self.questions)
        return result


def questions_response_from_dict(s: Any) -> QuestionsResponse:
    return QuestionsResponse.from_dict(s)


def questions_response_to_dict(x: QuestionsResponse) -> Any:
    return to_class(QuestionsResponse, x)
