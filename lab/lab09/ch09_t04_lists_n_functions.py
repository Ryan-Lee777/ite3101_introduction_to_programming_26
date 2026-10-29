# Write your function below!
from typ

def fizz_count(words: list) -> int:
    count = 0
    for word in words:
        if word == "fizz":
            count += 1
    return count
