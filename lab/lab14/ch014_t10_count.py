from typing import List


def count(sequence:List,item:any)->int:
    result = 0
    for i in sequence:
        if i == item:
            result += 1
    return result

