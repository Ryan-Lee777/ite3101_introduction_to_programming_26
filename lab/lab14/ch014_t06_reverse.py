def reverse(text:str)->str:
    word = ""
    n = len(text) - 1
    while n >= 0:
        word += text[n]
        n -= 1
    return word
