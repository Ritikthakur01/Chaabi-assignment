# Q1. Get your basics right - Implement selection sort algorithm in python. The function accepts a
# list in the input and returns a sorted list.
# E.g.
# Input f1([5,416,54,21,6135,15,741]) should
# Return [5, 15, 21, 54, 416, 741, 6135]

# <-------------Solution----------->

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        min_val = arr[i]
        for j in range(i + 1, n):
            if arr[j] < min_val:
                min_idx = j
                min_val = arr[j]

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

input_list = [5, 416, 54, 21, 6135, 15, 741]
sorted_list = selection_sort(input_list)
print(sorted_list)
