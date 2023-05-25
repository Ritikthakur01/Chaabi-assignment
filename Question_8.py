# Q8. Some neat tricks up her sleeve:
# Looking at the below code, write down the final values of A0, A1, ...An
# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A1 = range(10)
# A2 = sorted([i for i in A1 if i in A0])
# A3 = sorted([A0[s] for s in A0])
# A4 = [i for i in A1 if i in A3]
# A5 = {i:i*i for i in A1}
# A6 = [[i,i*i] for i in A1]
# A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
# A8 = map(lambda x: x*2, [1,2,3,4])
# A9 = filter(lambda x: len(x) >3, [“I” , “want”, “to”, “learn”, “python”])

# <---------------Solution---------------->
from functools import reduce

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A0 is a dictionary created by zipping together keys 'a', 'b', 'c', 'd', 'e' with corresponding values 1, 2, 3, 4, 5. So, the final value of A0 is {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.

A1 = range(10)
# A1 is assigned a range object from 0 to 9 (excluding 10). So, the final value of A1 is range(0, 10)

A2 = sorted([i for i in A1 if i in A0])
# Here, a list comprehension is used to filter elements from A1 that are present as keys in A0. Then, sorted() function is applied to sort the filtered elements. Since A0 only contains keys from 'a' to 'e', the final value of A2 will be an empty list, [].

A3 = sorted([A0[s] for s in A0])
# A list comprehension is used to create a new list by fetching values from A0 based on its keys. The resulting list is then sorted. Since the keys in A0 are 'a', 'b', 'c', 'd', 'e', the corresponding values are 1, 2, 3, 4, 5. Therefore, the final value of A3 will be [1, 2, 3, 4, 5].

A4 = [i for i in A1 if i in A3]
# A list comprehension is used to filter elements from A1 that are present in A3. Since A3 contains all values from 1 to 5, A4 will be a list containing those elements, [1, 2, 3, 4, 5].

A5 = {i:i*i for i in A1}
# A dictionary comprehension is used to create a new dictionary where each key i is paired with its square value i*i. Since A1 contains values from 0 to 9, the final value of A5 will be {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}.

A6 = [[i,i*i] for i in A1]
# A list comprehension is used to create a new list of lists, where each inner list contains an element i from A1 and its square value i*i. The final value of A6 will be [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]].

A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
# The reduce() function from the functools module is used with a lambda function that adds two numbers. The lambda function is applied to the list [10, 23, -45, 33] in a pairwise manner. So, the final value of A7 will be the sum of all the elements in the list, which is 21.

A8 = map(lambda x: x*2, [1,2,3,4])
# The map() function applies the lambda function that multiplies a number by 2 to each element in the list [1, 2, 3, 4]. So, the final value of A8 will be a map object containing the values [2, 4, 6, 8].

A9 = filter(lambda x: len(x) >3, ["I" , "want", "to", "learn", "python"])
# The filter() function applies the lambda function that checks if the length of a string is greater than 3 to each element in the list ["I", "want", "to", "learn", "python"]. It returns an iterator object that yields only the elements that satisfy the condition. So, the final value of A9 will be a filter object containing the values "want", "learn", and "python".

print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)
print(A7)
print(list(A8))
print(list(A9))

