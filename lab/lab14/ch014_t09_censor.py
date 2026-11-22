def censor(text:str,word:str)->str:
    result = []
    for char in text.split():
        if char == word:
            result.append("*" * len(word))