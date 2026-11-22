def factorial(x: int) -> int:
    total = 1
    for i in range(x):
        total = total * (i + 1)
    return total
