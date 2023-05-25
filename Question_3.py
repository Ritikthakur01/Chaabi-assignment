# Q3. Column Sorting, yay!

# Given a list of dicts, write a program to sort the list according to a key given in input.
# E.g.
# Input f([
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"}
# ], "fruit")
# Should Output
# [
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"},
# {"fruit": "orange", "color": "orange"}
# ]
# AND
# Input f([
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"}
# ], "color")
# Should Output
# [
# {"fruit": "blueberry", "color": "blue"},
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"}
# ]

# <---------------------Solution------------------->

from operator import itemgetter

def sort_list_of_dicts(lst, key):
    return sorted(lst, key=itemgetter(key))

def test_sort_list_of_dicts():
    lst1 = [
        {"fruit": "orange", "color": "orange"},
        {"fruit": "apple", "color": "red"},
        {"fruit": "banana", "color": "yellow"},
        {"fruit": "blueberry", "color": "blue"}
    ]
    key1 = "fruit"
    sorted_lst1 = sort_list_of_dicts(lst1, key1)
    print(sorted_lst1)
    
    lst2 = [
        {"fruit": "orange", "color": "orange"},
        {"fruit": "apple", "color": "red"},
        {"fruit": "banana", "color": "yellow"},
        {"fruit": "blueberry", "color": "blue"}
    ]
    key2 = "color"
    sorted_lst2 = sort_list_of_dicts(lst2, key2)
    print(sorted_lst2)

test_sort_list_of_dicts()

