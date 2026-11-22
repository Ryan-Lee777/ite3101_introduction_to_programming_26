from typing import List


def median(x: List[]) -> float:
    new = sorted(x)
    if len(x) % 2 != 0:
        n = len(x) // 2
        return new[n]
    else:
        m = len(x) // 2
        return (new[m] + new[m-1]) / 2.0
