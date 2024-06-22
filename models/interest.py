import dataclasses
from typing import Optional, List, Any, Dict

from models.utils import from_str, from_none, from_union, from_int, from_bool, from_dict, from_list


@dataclasses.dataclass
class Interest:
    id: Optional[str] = None
    category: Optional[str] = None
    interest: Optional[str] = None
    name: Optional[str] = None
    allow_images: Optional[bool] = None
    num_followers: Optional[int] = None
    num_questions: Optional[int] = None
    num_questions_per_language: Optional[Dict[str, int]] = None
    similar: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Interest':
        assert isinstance(obj, dict)
        _id = from_union([from_str, from_none], obj.get("_id"))
        category = from_union([from_str, from_none], obj.get("category"))
        interest = from_union([from_str, from_none], obj.get("interest"))
        name = from_union([from_str, from_none], obj.get("name"))
        allow_images = from_union([from_bool, from_none], obj.get("allowImages"))
        num_followers = from_union([from_int, from_none], obj.get("numFollowers"))
        num_questions = from_union([from_int, from_none], obj.get("numQuestions"))
        num_questions_per_language = from_union([lambda x: from_dict(from_int, x), from_none],
                                                obj.get("numQuestionsPerLanguage"))
        similar = from_union([lambda x: from_list(from_str, x), from_none], obj.get("similar"))
        return Interest(_id, category, interest, name, allow_images, num_followers, num_questions,
                        num_questions_per_language, similar)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["_id"] = from_union([from_str, from_none], self.id)
        if self.category is not None:
            result["category"] = from_union([from_str, from_none], self.category)
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
