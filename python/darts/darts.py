from math import hypot
def score(x, y):
    distance = 0
    if x == 0 or y == 0:
        distance = x + y
    else:
        distance = hypot(x, y)

    if distance <= 1:
        scored = 10
    elif 1 < distance <= 5:
        scored = 5
    elif 5 < distance <= 10:
        scored = 1
    else:
        scored = 0
    return scored