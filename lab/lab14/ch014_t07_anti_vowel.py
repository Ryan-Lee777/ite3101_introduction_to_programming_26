def anti_vowel(text:str) ->str:
    word = ""
    for i in text:
        if i != "A" and i != "a" and i != "E" and i != "e" and i != "I" and i != "i" and i != "O" and i != "o" and i != "U" and i != "u":
            word += i