vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"


def contains_vowels():
    return any(char in vowels for char in pwd)


def has_three_consecutive():
    for i in range(len(pwd) - 2):
        if all(char in vowels for char in pwd[i:i + 3]) or all(char in consonants for char in pwd[i:i + 3]):
            return True
    return False


def has_double_letter():
    for i in range(len(pwd) - 1):
        if pwd[i] == pwd[i + 1] and pwd[i] != "e" and pwd[i] != "o":
            return True
    return False


pwd = input()
while pwd != "end":
    if not contains_vowels() or has_three_consecutive() or has_double_letter():
        print(f"<{pwd}> is not acceptable.")
    else:
        print(f"<{pwd}> is acceptable.")
    pwd = input()
