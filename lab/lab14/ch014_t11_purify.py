from typing import List


def purify(x:List)->List:
    result = []
    for i in x:
        if i % 2 == 0:
        result.append(x[i])
    return result
