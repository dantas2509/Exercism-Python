def find_anagrams(word, candidates):
    ret = list()
    for candidate in candidates:
        auxWord = list(word.upper())
        auxCandidate = list(candidate.upper())
        for letter in candidate.upper():
            if letter in auxWord:
                auxWord.remove(letter)
                auxCandidate.remove(letter)
            else:
                break
        if len(auxWord) == len(auxCandidate) == 0 and word.upper() != candidate.upper():
            ret.append(candidate)

    return ret