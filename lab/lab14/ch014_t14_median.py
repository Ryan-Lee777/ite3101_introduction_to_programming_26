from typing import List


def median(x: List):
    new = x.sorted()
    if len(x) % 2 != 0:
        n = int(len(x) / 2)
        return new[n]
    else:
        m = len(x) / 2
        result = (new[m] + new[m-1]) / 2
        return result
