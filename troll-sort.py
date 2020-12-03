import random

def trollsort(ints):
    # Randomly select a sorting algorithm
    algSelection = random.randint(0, 1)

    if algSelection == 0:
        # print('Using bubble sort')
        bubble_sort(ints)
    if algSelection == 1:
        # print('Using merge sort')
        merge_sort(ints)

def bubble_sort(ints):
    # Modified from https://www.geeksforgeeks.org/bubble-sort/
    n = len(ints)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if ints[j] > ints[j+1] :
                ints[j], ints[j+1] = ints[j+1], ints[j]

def merge_sort(ints):
    print('Using merge sort')

ints = [1, 2]
ints = [64, 34, 25, 12, 22, 11, 90]

trollsort(ints)

for elem in ints:
    print(elem)
