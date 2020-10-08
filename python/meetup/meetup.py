from datetime import timedelta, date
from calendar import month_name
from num2words import num2words


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):
    weekDelta = timedelta(days=7)
    meetupDate = date(year, month, 1)

    # Looking for the first day of the week in the month
    while meetupDate.strftime('%A') != day_of_week:
        meetupDate += timedelta(days=1)

    if week[0].isdigit():
        meetupDate += (weekDelta * (int(week[0]) - 1))
        if meetupDate.month == month:
            return meetupDate
        else:
            raise MeetupDayException(f'there is no {week} {day_of_week} in {month_name[month]}')
    elif week == 'last':
        aux = meetupDate
        while True:
            aux += weekDelta
            if aux.month == month:
                meetupDate = aux
            else:
                return meetupDate
    elif week == 'teenth':
        while num2words(meetupDate.day)[-4:] != 'teen':
            meetupDate += weekDelta
        return meetupDate