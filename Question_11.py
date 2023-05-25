# Q11. Something fishy there -
# Find output of following:
# def f(x,l=[]):
# for i in range(x):
# l.append(i*i)
# print(l)
# f(2)
# f(3,[3,2,1])
# f(3)

# <-------------Solution------------>

def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1])
f(3)

# f(2)

# x is 2.
# Since no value is provided for l, it takes the default value, which is an empty list [].
# It iterates from 0 to 1 and appends the square of each value to the list l.
# The list l becomes [0, 1] and is printed.
# Output: [0, 1]

# f(3, [3, 2, 1])

# x is 3.
# The value [3, 2, 1] is explicitly provided for l.
# It iterates from 0 to 2 and appends the square of each value to the list l.
# The list l becomes [3, 2, 1, 0, 1, 4] and is printed.
# Output: [3, 2, 1, 0, 1, 4]

# f(3)

# x is 3.
# Since no value is provided for l, it takes the default value, which is the list modified in the previous call ([3, 2, 1, 0, 1, 4]).
# It iterates from 0 to 2 and appends the square of each value to the list l.
# The list l becomes [3, 2, 1, 0, 1, 4, 0, 1, 4] and is printed.
# Output: [3, 2, 1, 0, 1, 4, 0, 1, 4]