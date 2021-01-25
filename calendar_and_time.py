import calendar
import datetime
import time

print(calendar.weekheader(3))
print()

print(calendar.month(2019,3))

print(calendar.calendar(2020))

day_of_the_week= calendar.weekday(2020,10,2)
print(day_of_the_week)
# 4 means friday

is_leap=calendar.isleap(2019)
print(is_leap)

is_leap=calendar.isleap(2020)
print(is_leap)

how_many_leap_days=calendar.leapdays(2000,2021)
print(how_many_leap_days)



