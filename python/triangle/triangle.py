def equilateral(sides):
    return isTriangle(sides) and sides.count(sides[0]) == 3


def isosceles(sides):
    return isTriangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    return isTriangle(sides) and len(set(sides)) == 3

def isTriangle(sides):
    sides.sort()
    return len(sides) == 3 and sides.count(0) == 0 and sides[0] + sides[1] >= sides[2]