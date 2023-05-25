# Q10. Of date and days
# Write a func that takes 2 args:
# date - string representing a date in the form of 'yy-mm-dd'
# n - integer
# Returns the string representation of date n days before 'date'
# E.g. f('16-12-10', 11) should return '16-11-29'

# <------------Solution-------------->

from datetime import datetime, timedelta

def get_date_before(date, n):
    date_format = '%y-%m-%d'
    given_date = datetime.strptime(date, date_format)
    new_date = given_date - timedelta(days=n)
    return new_date.strftime(date_format)

# Example usage
date = '16-12-10'
n = 11

result = get_date_before(date, n)
print(result)
