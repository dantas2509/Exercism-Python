def is_valid(isbn):
    from functools import reduce
    import string

    isbn = isbn.replace('-', '')
    if len(isbn) != 10 or not isbn[:-1].isnumeric() or isbn[-1] not in string.digits + 'X':
        return False
    else:
        weights = range(10, 0, -1)
        digits = [10 if dig == 'X' else int(dig) for dig in isbn.replace('-', '')]
        return reduce(lambda x, y: (x[0]*x[1] + y[0] * y[1], 1), zip(digits, weights))[0] % 11 == 0