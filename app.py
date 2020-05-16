from python_examples import *
from timer import calcTime

my_list = [1, 3, 5, 7, 9]

# calcTime(binary_search(my_list, 3))

if __name__ == '__main__':
    arrSizes = list(range(5000,100000,10000))
    #arrSizes = [5,20,40]
    repetitions = 2

    for size in arrSizes:
        codeToSetup = '''
import time, timeit, random
from selectionsort import selectionSort
testArr = random.sample(range(1, 100000), {})
'''.format(size)
        print("Now running selectionSort with {}".format(size))
        codeToRun = '''
selectionSort(testArr)
'''
        res = calcTime(codeToRun, codeToSetup,repetitions)
        with open('''timekeeper/resultfiles/selectionSort.csv''', "a") as myfile:
            myfile.write("{},     {},     {}\n".format("selectionSort()",size,res))
            myfile.close()