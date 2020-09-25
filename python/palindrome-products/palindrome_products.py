def largest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError('min_factor is bigger than max_factor!')
    largestPalindrome = 0
    factor = list()
    for i in range(max_factor, min_factor - 1, -1):
        if i * max_factor < largestPalindrome:
            break
        for j in range(max_factor, min_factor - 1, -1):
            aux = i * j
            if aux < largestPalindrome:
                break
            if ''.join(reversed(str(aux))) == str(aux):
                if largestPalindrome == 0 or aux > largestPalindrome:
                    largestPalindrome = aux
                    factor = [[i, j]]
                elif aux == largestPalindrome and [j, i] not in factor:
                    factor.append([i, j])
    return largestPalindrome if largestPalindrome > 0 else None, factor


def smallest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError('min_factor is bigger than max_factor!')
    smallestPalindrome = 0
    factor = list()
    for i in range(min_factor, max_factor + 1):
        if i * min_factor > smallestPalindrome > 0:
            break
        for j in range(min_factor, max_factor + 1):
            aux = i * j
            if aux > smallestPalindrome > 0:
                break
            if ''.join(reversed(str(aux))) == str(aux):
                if smallestPalindrome == 0 or aux < smallestPalindrome:
                    smallestPalindrome = aux
                    factor = [[i, j]]
                elif aux == smallestPalindrome and [j, i] not in factor:
                    factor.append([i, j])
    return smallestPalindrome if smallestPalindrome > 0 else None, factor
