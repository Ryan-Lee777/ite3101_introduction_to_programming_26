def digit_sum(n: int) -> int:
    sum = 0
    for i in str(n):
        sum += int(i)