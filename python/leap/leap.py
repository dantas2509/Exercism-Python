def leap_year(year):
    isLeapYear = False

    if year % 4 == 0:
        if year % 100 == 0 and not(year % 400 == 0):
            isLeapYear = False
        else:
            isLeapYear = True

    return isLeapYear