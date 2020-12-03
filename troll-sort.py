import random

def troll_sort(ints):
    # Randomly select a sorting algorithm
    algSelection = random.randint(0, 2)

    if algSelection == 0:
        print('Using bubble sort')
        bubble_sort(ints)
    if algSelection == 1:
        print('Using merge sort')
        merge_sort(ints)
    else:
        while True:
            print("You've just been trolled!  Okay, I'll be nice: press CTRL+C to stop.")

def bubble_sort(ints):
    # print('Using bubble sort')
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
    # print('Using merge sort')

    # Modified from https://www.geeksforgeeks.org/merge-sort/
    if len(ints) > 1:

         # Finding the mid of the array
        mid = len(ints)//2

        # Dividing the array elements
        L = ints[:mid]

        # into 2 halves
        R = ints[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                ints[k] = L[i]
                i += 1
            else:
                ints[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            ints[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            ints[k] = R[j]
            j += 1
            k += 1

#ints = [1, 2]
#ints = [64, 34, 25, 12, 22, 11, 90]

ints = [12, 11, 13, 5, 6, 7]

troll_sort(ints)

print(ints)
