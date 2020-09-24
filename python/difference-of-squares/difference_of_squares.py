from functools import reduce
def square_of_sum(number):
    return reduce(lambda x, y: x+y, range(0, number+1)) ** 2


def sum_of_squares(number):
    return reduce(lambda x, y: x + y ** 2, range(0, number + 1))


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)