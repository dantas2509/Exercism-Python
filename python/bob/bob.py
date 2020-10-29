import re
import string


def response(hey_bob):
    hey_bob = hey_bob.strip()
    if len(hey_bob) > 0:
        if hey_bob[-1] == '?':  #Question
            if re.search(r'[a-z]', hey_bob) or not re.sub(r'[\W|\d]', '', hey_bob):  # Not Yelling
            #if re.search(r'[^A-Z]', re.sub(r'\W', '', hey_bob)) or not re.sub(r'\W', '', hey_bob):  # Not Yelling
                return 'Sure.'
            else:
                return "Calm down, I know what I'm doing!"
        else:
            if re.search(r'[a-z]', hey_bob) or not re.sub(r'[\W|\d]', '', hey_bob):  # Not Yelling
                return 'Whatever.'
            else:
                return 'Whoa, chill out!'
    else:
        return 'Fine. Be that way!'