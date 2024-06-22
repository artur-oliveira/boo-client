from datetime import datetime
from enum import Enum
from typing import Any, List, TypeVar, Type, Callable, cast, Dict

import dateutil.parser

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_none(x: Any) -> Any:
    is_none = x is None
    if not is_none and x is not None:
        raise AssertionError(f'cant call from_none of obj {x}')
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except ValueError as ex:
            if x is not None:
                raise ex
        except (AssertionError, TypeError):
            ...
    assert False


def from_int(x: Any) -> int:
    is_int = isinstance(x, int) and not isinstance(x, bool)
    if not is_int and x is not None:
        raise AssertionError(f'{x} is not int')
    assert is_int
    assert x is not None
    return x


def from_str(x: Any) -> str:
    is_str = isinstance(x, str)
    if not is_str and x is not None:
        raise AssertionError(f'{x} is not str')
    assert is_str
    assert x is not None
    return x


def from_float(x: Any) -> float:
    is_float = isinstance(x, (float, int)) and not isinstance(x, bool)
    if not is_float and x is not None:
        raise AssertionError(f'{x} is not float')
    assert is_float
    assert x is not None
    return float(x)


def from_bool(x: Any) -> bool:
    is_bool = isinstance(x, bool)
    if not is_bool and x is not None:
        raise AssertionError(f'cant call from_bool in obj {x}')
    assert is_bool
    assert x is not None
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    is_dict = isinstance(x, dict)
    if not is_dict and x is not None:
        raise AssertionError(f'cant call from_dict in obj {x}')
    assert is_dict
    assert x is not None
    return {k: f(v) for (k, v) in x.items()}


def to_float(x: Any) -> float:
    is_float = isinstance(x, (int, float))
    if not is_float and x is not None:
        raise AssertionError(f'cant call to_float in obj {x}')
    assert is_float
    assert x is not None
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    is_enum = isinstance(x, c)
    if not is_enum and x is not None:
        raise AssertionError(f'cant call to_enum in obj {x}')
    assert is_enum
    assert x is not None
    return x.value


def is_type(t: Type[T], x: Any) -> T:
    is_type_ = isinstance(x, t)
    if not is_type_ and x is not None:
        raise AssertionError(f'cant call is_type in obj {x}')
    assert is_type_
    assert x is not None
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    is_list = isinstance(x, list)
    if not is_list and x is not None:
        raise AssertionError(f'cant call from_list in obj {x}')
    assert is_list
    assert x is not None
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    is_class = isinstance(x, c)
    if not is_class and x is not None:
        raise AssertionError(f'cant call to_class in obj {x}')
    assert is_class
    assert x is not None
    return cast(Any, x).to_dict()


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)
