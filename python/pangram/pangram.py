def is_pangram(sentence):
    import string
    alphabet = list(string.ascii_lowercase)
    
    alphabet = ''.join(filter(lambda x: x not in sentence.lower(), alphabet))
    
    #alphabet = list(range(ord('a'),ord('z')+1))
    
    #for l in sentence.lower():
    #    if ord(l) in alphabet:
    #        alphabet.remove(ord(l))
    
    return len(alphabet) == 0
