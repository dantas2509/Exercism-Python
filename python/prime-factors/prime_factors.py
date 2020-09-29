def factors(value):
    prime_factors = list()
    factor = 2
    while factor ** 2 <= value:
        if value % factor == 0:
            value /= factor
            prime_factors.append(factor)
        else:
            factor += 1
    if value > 1:
        prime_factors.append(int(value))
    return prime_factors
