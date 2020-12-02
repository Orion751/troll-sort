# import random

def trollsort(ints):
    for elem in ints:
        print(elem)

    '''
    Randomly select a sorting algorithm
    algSelection = random.randint(0, 1)

    if algSelection == 0:
        print('Using bubble sort')
        bubble_sort(ints)
    if algSelection == 1:
        print('Using merge sort')
        merge_sort(ints)

    '''

def bubble_sort(ints):
    print('Using bubble sort')

def merge_sort(ints):
    print('Using merge sort')

ints = [1, 2]

trollsort(ints)
