def countdown(i):
    print(i)
    if i < 0:  # base case - stop if
        return
    else:
        countdown(i-1)  # recursive case - calls itself


countdown(10)

'''
10
9
8
7
6
5
4
3
2
1
0
-1
'''
