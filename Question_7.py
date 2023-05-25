# Q7. Calculate the factorial of a number using lambda function.

# <---------------Solution--------------->

from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

number = 5
result = factorial(number)
print(result)
