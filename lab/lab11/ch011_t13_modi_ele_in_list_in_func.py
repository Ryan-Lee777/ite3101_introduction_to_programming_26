from typing import List


n = [3, 5, 7]


for i in range(0, len(n)):
    n[0] = n[0] * 2
    

def double_list(x: List) -> List:
    y = []
    for i in range(0, len(x)):
        y.append(x[i] * 2)
    return y


print(double_list(n))

# Don't forget to return your new list!

# print(double_list(n))
