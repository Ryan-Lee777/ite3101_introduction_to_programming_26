answer = "Tis but a scratch!"


def black_knight() -> bool:
    if answer == "Tis but a scratch!":
        return 'False'
    else:
        return 'True'


def french_soldier() -> bool:
    if answer == "Go away, or I shall taunt you a second time!":
        return 'True'
    else:
        return 'False'

print(black_knight())
print(french_soldier())    