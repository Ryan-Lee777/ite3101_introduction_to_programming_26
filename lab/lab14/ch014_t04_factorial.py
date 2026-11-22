def factorial(x: int) -> int:
    total = 0
    for i in range(x):
        total = total * (int(i) + 1)
    return total
factorial(4)