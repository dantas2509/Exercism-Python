def steps(number):
    if number > 0:
        steps = 0
        while number > 1:
            number = number / 2 if number % 2 == 0 else (number * 3) + 1
            steps += 1
        return steps
    else:
        raise ValueError('Number is zero or negative!')
