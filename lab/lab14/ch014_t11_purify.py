from typing import List


def purify(x:List)->List:
    result = []
    for i in x:
        result.append(x[i])
    return result
