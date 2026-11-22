from typing import List


def product(x:List[int])->int:
    result = 1
    for i in x:
        result *= i
    return result
