
# 4.1: Write out the code for the earlier sum function:
numList = [1, 2, 3, 4, 5, 6]

def sumList(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

print('sumList', sumList(numList))

# print(numList[1:]) returns [2, 3, 4, 5, 6] - i.e. from index 1 onwards


# 4.2: Write a recursive function to count the number of items in a list.

def countList(arr):
    if arr == []:
        return 0
    return 1 + countList(arr[1:])

print('countList', countList(numList))

# 4.3: Find the maximum number in a list.

# base case = []
# [5]

numList = [1, 2, 3, 4, 5, 6]

def maxNum(arr):
    if len(arr) == 2: #i.e. only two left
        return  arr[0] if arr[0] > arr[1] else arr[1]
    max = maxNum(arr[1:])
    return arr[0] if arr[0] > max else max

print('maxNum', maxNum(numList))