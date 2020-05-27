# Experiments with Algorithms

Trying out the algorithm examples in Aditya Bhargava's *Grokking Algorithms*. Translating them from Python into Ruby (and back again) to ensure I fully understand them. 

[Chapter 1](#notes-on-chapter-1) | [Chapter 2](#notes-on-chapter-2) | [Chapter 3](#chapter-3) | 

## Notes on Chapter 1

### Solidifying my Understanding of Exponentials and Intro to Logarithms

**Exponentials**: 

10<sup>2</sup> = 10 * 10 = 100

10<sup>3</sup> = 10 * 10 * 10 = 1000

10<sup>10</sup> = 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10  *or (10 * 10 ten times)* = 10bil

**Logarithms**:

Expenentials flipped. 

10<sup>2</sup> = 100 <---> log<sub>10</sub> 100 = 2 (i.e. 10 * 10 = 100)

10<sup>3</sup> = 1000 <---> log<sub>10</sub> 1000 = 3 (i.e. 10 * 10 = 100)

2<sup>3</sup> = 8 <---> log<sub>2</sub> 8 = 3 (i.e. 2 * 2 * 2 = 8)

When discussing Big O notation in the book log always means log<sub>2</sub> 

### Big O Notation 

Simple search = going through list one by one. O(n) - i.e. the max number of times you have to iterate through the list is equal to the length the list. 

For list of 8 numbers, simple search = O(8)

Binary search = have to check max log n. 

For list of 8, binary = O(log<sub>3</sub>) i.e. 3 guesses max. 

## Notes on Chapter 2

Arrays have fast reads and slow inserts. Linked lists have slow reads and fast inserts.

**Selection Sort**:
Strange concept covered more in chapter 3...
Sorting a list of 7 songs with play counts. To sort in order you iterate over the list 7 times to find most played, push that into new list then iterate over the remaining songs to find the next most played. Repeat until list sorted. 

This is O(n<sup>2</sup>)...even though really you only check the list half that number of times on average. QUE?? It says this is because O notation ignores half numbers...'constants like 1/2 are ignored in Big O notation'. 


## Chapter 3

### Recursion ### 

Recursion = when a function calls itself. 

e.g. this pseudocode:
```def look_for_key(box):
for item in box:
  if item.is_a_box():
    look_for_key(item) <-- Recursion!
  elif item.is_a_key():
    print “found the key!”
```
Recursion is used when it makes the solution clearer. The above code is clearer than:

```
def look_for_key(main_box):
  pile = main_box.make_a_pile_to_look_through()
  while pile is not empty:
    box = pile.grab_a_box()
    for item in box:
      if item.is_a_box():
        pile.append(item)
      elif item.is_a_key():
        print “found the key!”
```

No performance benefit to using recursion, loops are actuslly faster sometimes. 

Quote by Leigh Caldwell on Stack Overflow: “Loops may achieve a performance gain for your program. Recursion may achieve a performance gain for your programmer. Choose which is more important in your situation!”

**Base Case & Recursive Case (AKA You must tell a recursive function when to stop)**

Example of a countdown fucntion:

```
def countdown(i):
print i
countdown(i-1)
```
This would count down forever. 

Therefore, every recursive function has two parts - the base case (when the function doesn’t call itself again) and the recursive case (when the function calls itself).

We can solve the above infinite loop by adding the base case:

```
def countdown(i):
  print i
  if i <= 0: <-- Base Case (stop if)
    return
  else: <-- Recursive case
    countdown(i-1)
```



