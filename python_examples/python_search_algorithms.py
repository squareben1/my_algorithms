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


def find_smallest(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index


def selection_sort(list):
    new_list = []
    for i in range(len(list)):
        smallest = find_smallest(list)
        new_list.append(list.pop(smallest))
    return new_list


'''
Exercise 4.1 -
Recursive Sum
'''


def recursive_sum(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + recursive_sum(list[1:])


'''
Exercise 4.2 -
Write a recursive function to count the number of items in a list
'''


def recursive_count(list):
    if list == []:
        return 0
    else:
        return 1 + recursive_count(list[1:])


'''
Exercise 4.3 -
Find the maximum number in a list
'''


def recursive_max_num(list):
    if len(list) == 1:
        return list[0]
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    else:
        next_max = recursive_max_num(list[1:])
        return list[0] if list[0] > next_max else next_max


'''
    Exercise 4.4 - Base case for recursive binary search:
    - array with 1 number in it

    Tried to replicate original below (i.e. return index)...
    #TODO return to this
'''


def recursive_binary(list, item):
    
    if len(list) == 0:
        return False
    else:
        index = 0
        midpoint = len(list) // 2

        if list[midpoint] == item:
            return list.index(item)+index
        else:
            if item < list[midpoint]:
                return recursive_binary(list[:midpoint],item)
            else:
                 return recursive_binary(list[midpoint:],item + midpoint)
    # if len(list) == 1:
    #     return list[0] if list[0] == item else False
    # else:
    #     mid = len(list)//2
    #     if item < list[mid]:
    #         return recursive_binary(list[:mid], item)
    #     else:
    #         return recursive_binary(list[mid+1:], item)

'''
QUICKSORT
'''

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        print('less:', less)
        greater = [i for i in array[1:] if i > pivot]
        print('greater:', greater)
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3, 11]))