def convert(number):
    ret = ''
    hasFactor = False
    sounds = {3:'Pling', 5: 'Plang', 7:'Plong'}
    for k, v in sounds.items():
        if number % k == 0:
            ret += v
            hasFactor = True
    return ret if hasFactor else str(number)
    
