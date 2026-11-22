from typing import List


def remove_duplicates(x:List[int])-> List:
    result = []
    for i in x:
        if i not in result:
            result.append(i)
    return result
