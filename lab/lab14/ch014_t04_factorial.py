def factorial(x:int)->int:
    total = 0
    for i in range(x):
        total *= (i + 1)
    return total
