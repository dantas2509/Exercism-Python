def is_armstrong_number(number):
    n = str(number)
    power = len(n)
    sum = 0

    for l in n:
        sum += int(l) ** power

    return sum == number

    