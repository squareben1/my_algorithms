# Experiments with Algorithms

Trying out the algorithm examples in Aditya Bhargava's *Grokking Algorithms*.  

[Chapter 1](#chapter-1) | [Chapter 2](#chapter-2---selection-sort) | [Chapter 3](#chapter-3---recursion) | [Chapter 4](#chapter-4---quicksort) | 

## Chapter 1

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

## Chapter 2 - Selection Sort

### Arrays & Linked Lists

Arrays have fast reads and slow inserts. Linked lists have slow reads and fast inserts.

**Arrays** = items stored next to each other in memory.

 **Arrays = Slow inserts** because, like at cinema when new person coems along, you have to move the whole array to somewhere it will fit if the next memory slot is taken. 

**Arrays = Fast Reads** Arrays are great if you want to read random elements, because you can look up any element in your array instantly.

**Linked Lists = Slow Reads** = items stored at different places in memory with each item pointing to location of next. Like a treasure hunt. 

Like a Top 10 best blah blah list where you have to click through to get to end  

**Linked Lists = Fast inserts** because you can put new items anywhere and store the location with the previous item. Never have to move. 
**Fast Deletions** too as just have to change what teh previous element points to.

**Arrays = We all need to move down - there's a four over there**

**Linked Lists = “Let’s split up and watch the film.”**



### Selection Sort:
Strange concept covered more in chapter 3...
Sorting a list of 7 songs with play counts. To sort in order you iterate over the list 7 times to find most played, push that into new list then iterate over the remaining songs to find the next most played. Repeat until list sorted. 

This is O(n<sup>2</sup>)...even though really you only check the list half that number of times on average. QUE?? ANSWER: this is because O notation ignores half numbers...'constants like 1/2 are ignored in Big O notation'. 

**Revisiting**: You check a list O(n) times, then check it O(n-1) times, O(n-2) times and so on. in theory therefore you actually check it O(n...and a half) times. BUT constants like 1/2 are ignored in Big O notation. 


## Chapter 3 - Recursion

### Recursion ### 

Recursion = when a function calls itself. 

e.g. this pseudocode:
```
def look_for_key(box):
  for item in box:
    if item.is_a_box():
      look_for_key(item) <--Recursion!
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

### Factorial ###

```factorial(5)``` is written as ```5!```, and it’s
defined like this: ```5! = 5 * 4 * 3 * 2 * 1```.

### The Stack ###

Push & pop. 

All function calls go on the stack.

Using the example of searchign for a key in a box containing many boxes (which each potentially hold a box) you dont need to keep track of a pile of boxes, the stack does it for you. 

This can be memory intensive. If you dont include a break clause it could go on forever (until the computer runs out of memory anyway). It will then exit with a stackoverflow error.  

## Chapter 4 - Quicksort

COME BACK TO: WHAT IS O(n log n)

### Divide & Conquer

1. Work out a simple base case

2. Work out how to reduce the problem and get to the base case. 

In the example we are dividing a farmer's plot of land. 

Plot measures 1680 x 640. Start by finding the biggest square possible (the smallest side by the smallest side). 

2 x 640 plots leaves 400 x 640. 

Find the two biggest squares in that (400 x 400, leaves 240 x 400). 

Keep doing this until you get down to 80 x 160. 80 x 2 = 160 so **base base is 80**.

The biggest square plot of land possible is 80x80.

**Using Recursion**

Take this simple function:
```
def sum(arr):
    total = 0
    for x in arr:
    total += x
    return total
print sum([1, 2, 3])
```

This can be done with recursion. Simplest case would be **one** or **zero** items in array. 
```
Sum([]) - 0 elements = 0
Sum([7]) - 1 element = 7
```

Therefore this is the base case. We need to move closer to the above with each recursive call. 

```
sum([2, 4, 6])  ->  (working back up: **12**)

2 + sum([4, 6])  ->  (working back up: 10 + 2)

4 + sum([6])  ->  (working back up: 6 + 4)

sum([6])
```

^ BASE CASE, recursion keeps track of state(stack) and works way back up. 

**Tip**
When you’re writing a recursive function involving an array, the base case is often an empty array or an array with one element. If you’re stuck, try that first.

*See exercises/chapter_4.py*

### Quicksort

continue on page60