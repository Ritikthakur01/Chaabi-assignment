# Q9.
# Write a func that takes 3 args:
# from_date - string representing a date in the form of 'yy-mm-dd'
# to_date - string representing a date in the form of 'yy-mm-dd'
# difference - int
# Returns True if from_date and to_date are less than difference days away from each other, else
# returns False.

# <------------Solution------------->

from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    date_format = '%y-%m-%d'
    date1 = datetime.strptime(from_date, date_format)
    date2 = datetime.strptime(to_date, date_format)
    date_difference = abs(date2 - date1).days
    return date_difference < difference

# Example usage
from_date = '21-05-10'
to_date = '21-05-15'
difference = 10

result = check_date_difference(from_date, to_date, difference)
print(result)
