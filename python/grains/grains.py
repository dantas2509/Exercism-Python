def square(number):
    if 0 < number <= 64:
        return pow(2, number-1)
    else:
        raise ValueError('The number has to be greater than 0 and less than 65!')


def total():
    return (square(64) * 2) - 1
