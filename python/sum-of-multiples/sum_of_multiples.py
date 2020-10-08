def sum_of_multiples(limit, multiples):
    return sum(
        [num for num in range(limit) if len([num for multi in multiples if multi > 0 and num % multi == 0]) > 0])
