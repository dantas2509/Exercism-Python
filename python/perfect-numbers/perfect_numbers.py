from functools import reduce
def classify(number):
    if number <= 0:
        raise ValueError('Only positve numbers.')
    elif number == 1:
        return 'deficient'
    quo = reduce(lambda x, y: x+y, [x for x in range(1, number) if number % x == 0])
    if quo < number: return 'deficient'
    elif quo == number: return 'perfect'
    else: return 'abundant'