from typing import List


n = [3, 5, 7]


def total(numbers: List[int]) -> List[int]:
    result = 0
    for i in range(len(numbers)):
        result += numbers[0]
    return result
