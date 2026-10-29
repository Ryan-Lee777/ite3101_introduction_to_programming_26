# Write your function below!
def fizz_count(words: LIST) -> int:
    count = 0
    for word in words:
        if word == "fizz":
            count += 1
    return count
