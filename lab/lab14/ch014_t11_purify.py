from typing import List


def purify(x:List)->List:
    result = []
    for i in range(1,len(x)):
        result.append(i)
    return result
