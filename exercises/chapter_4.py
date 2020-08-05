
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

# 4.4 What is the base case and recursive case for binary search?

# "Remember binary search from chapter 1? It’s a divide-and conquer
# algorithm, too. Can you come up with the base case and recursive case 
# for binary search?"

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) / 2
        guess = list[mid] 
        if guess == item: # BASE CASE
            return mid
        if guess > item: # here = recursive 
            high = mid - 1
        else:
            low = mid + 1

# So I said base case was the item == list[mid] and the recursive 
# was splitting the array in two and repeating...
# 
# ANSWER: "The base case for binary search is an array with one item.
# If the item you’re looking for matches the item in the array, you
# found it! Otherwise, it isn’t in the array.
# In the recursive case for binary search, you split the array in half,
# throw away one half, and call binary search on the other half.

# SO: 

def recursive_binary(arr, low, high, item):
    if high >= low: #check base case
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return recursive_binary(arr, low, mid-1, item)
        else:
            return recursive_binary(arr, mid+1, high, item)
    
print('recursive_binary', recursive_binary(numList, 0, len(numList)-1, 3))
# == 2

