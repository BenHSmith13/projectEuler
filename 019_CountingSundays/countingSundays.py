__author__ = 'bensmith'

year = 1900
day = 1  # So % 7 == 0 means sunday
sundays = 0

while year < 2001:
    month = 1  # 1 = January, 2 February...
    while month < 13:
        if year > 1900:  # this is to exclude any data from 1900
            if day % 7 == 0:
                sundays += 1
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            day += 31
            month += 1
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day += 30
            month += 1
        elif month == 2:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        day += 29
                        month += 1
                    else:
                        day += 28
                        month += 1
                else:
                    day += 29
                    month += 1
            else:
                day += 28
                month += 1
    year += 1

print(sundays)