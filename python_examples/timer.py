import time, timeit
# import * from python_search_algorithms

def calcTime(algorithm, codeToSetup, repeat):
    res = timeit.repeat(stmt = algorithm, setup = codeToSetup, number = 1, repeat = repeat)
    sum = 0
    for x in res:
        sum = sum + x
    x = sum / repeat
    return x

calcTime(PySe)