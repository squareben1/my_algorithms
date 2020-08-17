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


def recursive_sum(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + recursive_sum(list[1:])


def recursive_count(list):
    if list == []:
        return 0
    else:
        return 1 + recursive_count(list[1:])


def recursive_max_num(list):
    if len(list) == 1:
        return list[0]
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    # else:
    #     next_max = recursive_max_num(list[1:])
    #     return list[0] if list[0] > next_max else next_max
    
