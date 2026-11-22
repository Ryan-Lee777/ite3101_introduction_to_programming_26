def anti_vowel(text:str) ->str:
    word = ""
    for i in text:
        if i.lower not in "aeiou":
            word += i
    return word
