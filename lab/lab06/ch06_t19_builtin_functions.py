from typing import Any


def distance_from_zero(a: Any) -> Any:
    if type(a) == int or type(a) == float:
        return abs(a)
    return "Nope"
