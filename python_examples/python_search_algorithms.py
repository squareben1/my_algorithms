import timeit

def linear_search(mylist, find):
    for x in mylist:
        if x == find:
            return True
    return False

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = round((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1


def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array):
    new_arr = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        new_arr.append(array.pop(smallest))
    return new_arr

def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else: 
        return arr[0] + recursive_sum(arr[1:])