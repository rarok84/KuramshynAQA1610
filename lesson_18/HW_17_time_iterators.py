import time
from datetime import timedelta
import datetime as dt
from random import randint

def calculate_date(year, month, day, hour, minute, second, microsecond, other_days, to_add):
    datetime = dt.datetime(year, month, day, hour, minute, second ,microsecond)
    days = dt.timedelta(other_days)
    add = to_add
    if add:
        return datetime + days
    else:
        return datetime - days

print(calculate_date(2012,9,15,12,12,12,12, 12, False))
print(calculate_date(2012,9,15,12,12,12,12, 12, True))

def calculate_age(year, month, day, hour, minute, second, microsecond):
    my_birth = dt.datetime(year, month, day, hour, minute, second ,microsecond)
    current_datetime = dt.datetime.now()
    return current_datetime - my_birth

print(calculate_age(1997,3,14,12,12,12,12,))
print(calculate_age(1997,3,14,12,12,12,12,).total_seconds())

def list_comprehension():
    rand_list = [*(randint(1, 10) for item in range(100)),]
    print(rand_list)
    for i in range(10):
        print(f"{i+1} occurrence: ", len([item for item in rand_list if item == i+1]))

list_comprehension()