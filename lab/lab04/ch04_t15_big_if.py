# Complete the if and elif statements!
def grade_converter(grade: int) -> str:
    if answer >= 90:
        return 'A'
    elif answer >= 80:
        return 'B'
    elif answer >= 70:
        return 'C'
    elif answer >= 65:
        return 'D'
    else:
        return 'F'


# This should print an "A"
print(grade_converter(92))

# This should print a "C"
print(grade_converter(70))

# This should print an "F"
print(grade_converter(61))
