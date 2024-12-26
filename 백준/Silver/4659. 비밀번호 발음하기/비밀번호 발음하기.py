vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
accept = "eo"


def contains_vowels(s):
    return any(char in vowels for char in s)


def has_three_consecutive(s):
    for i in range(len(s) - 2):
        if all(char in vowels for char in s[i:i + 3]) or all(char in consonants for char in s[i:i + 3]):
            return True
    return False


def has_double_letter(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] and s[i] not in accept:
            return True
    return False


pwd = input()
while pwd != "end":
    if not contains_vowels(pwd) or has_three_consecutive(pwd) or has_double_letter(pwd):
        print(f"<{pwd}> is not acceptable.")
    else:
        print(f"<{pwd}> is acceptable.")
    pwd = input()
