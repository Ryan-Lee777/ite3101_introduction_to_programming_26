def greater_less_equal_5(answer: int) -> int:
    if answer>90:
        return 'A'
    elif answer>=80:
        return 'B'
    elif answer>=70:
        return 'C'
    elif answer>=65:
            return 'B'
    elif answer>=80:
            return 'B'
    else:
        return 0


print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))
