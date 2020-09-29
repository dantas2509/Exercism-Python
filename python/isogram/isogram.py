def is_isogram(string):
    from string import ascii_uppercase

    letters = [letter for letter in string.upper() if letter in ascii_uppercase]
    return len(set(letters)) == len(letters)
