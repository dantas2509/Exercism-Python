def is_pangram(sentence):
    alphabet = list(range(ord('a'),ord('z')+1))
    
    for l in sentence.lower():
        if ord(l) in alphabet:
            alphabet.remove(ord(l))
    
    return len(alphabet) == 0
