# importing the required modules
import timeit

# binary search function


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # Check if x is present at mid
        if arr[mid] < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid] > x:
            high = mid - 1

        # If x is smaller, ignore right half
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


# linear se  arch function
def linear_search(mylist, find):
    for x in mylist:
        if x == find:
            return True
    return False


# compute binary search time
def binary_time():
    SETUP_CODE = ''' 
from __main__ import binary_search 
from random import randint'''

    TEST_CODE = ''' 
mylist = [x for x in range(10000)] 
item = randint(0, len(mylist)) 
binary_search(mylist, item)'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    # printing minimum exec. time
    print('Binary search time: {}'.format(min(times)))


# compute linear search time
def linear_time():
    SETUP_CODE = ''' 
from __main__ import linear_search 
from random import randint'''

    TEST_CODE = ''' 
mylist = [x for x in range(10000)] 
find = randint(0, len(mylist)) 
linear_search(mylist, find) 
	'''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=500)

    # priniting minimum exec. time
    print('Linear search time: {}'.format(min(times)))


if __name__ == "__main__":
    linear_time()
    binary_time()
