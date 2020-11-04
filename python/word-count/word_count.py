import re


def count_words(sentence):
    ret = dict()
    words = re.findall(r"\W?([a-zA-Z0-9]+('[a-zA-Z0-9])*)\W?", sentence.lower())
    words = [word[0] for word in words]

    for word in set([word.lower() for word in words]):
        ret[word] = words.count(word)

    return ret
