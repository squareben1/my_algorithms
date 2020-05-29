
# 4.1: Write out the code for the earlier sum function:
def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:]) 
    
numList = [1, 2, 3, 4, 5, 6]

print(sum(numList))

# print(numList[1:]) returns [2, 3, 4, 5, 6] - i.e. from index 1 onwards

