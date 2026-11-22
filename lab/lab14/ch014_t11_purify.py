from typing import List


def purify(x:List)->List:
    result = []
    for i in range(1,len(x)):
        result.append(x[i])
    return result
