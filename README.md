# Experiments with Algorithms

Trying out the algorithm examples in Aditya Bhargava's *Grokking Algorithms*.  


--------------

[Chapter 1](#chapter-1) | [Chapter 2](#chapter-2---selection-sort) | [Chapter 3](#chapter-3---recursion) | [Chapter 4](#chapter-4---quicksort) | 

## Chapter 1

### Exponentials and Intro to Logarithms

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

Big O notation lets you compare the number of operations. It tells you how fast the algorithm grows.

N = input size

Simple search = going through list one by one. O(n) - i.e. the max number of times you have to iterate through the list is equal to the length the list. 

For list of 8 numbers, simple search = O(8)

Binary search = have to check max log n. 

For list of 8, binary = O(log<sub>3</sub>) i.e. 3 guesses max (divide it 3 times)

List of 1024: O(log<sub>10</sub>) i.e. in worst case have to divide it 10 times. 

#### Travelling Salesperson

Work out quickest journey time between 5 cities. 120 permutations. 

For n items, it will take n! (n factorial) operations to
compute the result. 

So this is O(n!) time, or factorial time.

There are 120 permutations with 5 cities, so it will
take 120 operations to solve the problem for 5 cities. For 6 cities, itwill take 720 operations (there are 720 permutations). For 7 cities, it will take 5,040 operations!

-------------

**Factorial!**

The factorial function (symbol: !) says to multiply all whole numbers from our chosen number down to 1.

Examples:

4! = 4 × 3 × 2 × 1 = 24

7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040

1! = 1

-------------

## Chapter 2 - Selection Sort

### Arrays & Linked Lists

Arrays have fast reads and slow inserts. Linked lists have slow reads and fast inserts.

|           | Arrays | Lists |
| --------- | ------ | ----- |
| Reading   | O(1)   | O(n)  |
| Insertion | O(n)   | O(1)  |
| Deletion  | O(n)   | O(1)  |

Question: Why do arrays have deletion of O(1) - unless this means only the first or last? Fast deletion as 'just have t change what previous element points to' - how does this make sense though? Surey you need to find it before you can delete it...??

**Arrays** = items stored next to each other in memory.

 **Arrays = Slow inserts** because, like at cinema when new person comes along, you have to move the whole array to somewhere it will fit if the next memory slot is taken. 

**Arrays = Fast Reads** Arrays are great if you want to read random elements, because you can look up any element in your array instantly.

**Linked Lists = Slow Reads** = items stored at different places in memory with each item pointing to location of next. Like a treasure hunt. 

Like a Top 10 best blah blah list where you have to click through to get to end  

**Linked Lists = Fast inserts** because you can put new items anywhere and store the location with the previous item. Never have to move. 
**Fast Deletions** too as just have to change what the previous element points to.
**Question: But how do you find it to delete it in the first place?** 

**Arrays = We all need to move down - there's a four over there**

**Linked Lists = “Let’s split up and watch the film.”**

Note: All elements in the array should be the same type (all ints, all doubles, and so on).


### Selection Sort:
Strange concept covered more in chapter 3...
Sorting a list of 7 songs with play counts. To sort in order you iterate over the list 7 times to find most played, push that into new list then iterate over the remaining songs to find the next most played. Repeat until list sorted. 

This is O(n<sup>2</sup>)...even though really you only check the list half that number of times on average. QUE?? ANSWER: this is because O notation ignores half numbers...'constants like 1/2 are ignored in Big O notation'. 

**Revisiting**: You check a list O(n) times, then check it O(n-1) times, O(n-2) times and so on. In theory therefore you actually check it O(n...and a half) times. BUT constants like 1/2 are ignored in Big O notation. 


## Chapter 3 - Recursion

### Recursion ### 

Recursion = when a function calls itself.

```
“Recursion is when a function calls itself until it doesn’t.”

— Mattias Petter Johansson
```

e.g. this pseudocode:
```
def look_for_key(box):
  for item in box:
    if item.is_a_box():
      look_for_key(item) # <--Recursion!
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

Using the example of searching for a key in a box containing many boxes (which each potentially hold a box) you dont need to keep track of a pile of boxes, the stack does it for you. 

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

```
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        print('less:', less)
        greater = [i for i in array[1:] if i > pivot]
        print('greater:', greater)
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3, 11]))

less: [5, 2, 3]
greater: [11]
less: [2, 3]
greater: []
less: []
greater: [3]
[2, 3, 5, 10, 11]

```

If you’re implementing quicksort, choose a **random** element as the
pivot. The average runtime of quicksort is O(n log n).

## Hash Tables

Key Value pairs. 

Looking something up in a hash table takes constant time O(1).

Hash tables in Python:

```
book = dict() 
or
phone_book = {}

book[“apple”] = 0.67
book[“milk”] = 1.49
book[“avocado”] = 1.49

print book
{‘avocado’: 1.49, ‘apple’: 0.67, ‘milk’: 1.49}
```

Recap:

Hashes are good for...

- Modeling relationships from one thing to another thing

- Filtering out duplicates

- Caching/memorizing data instead of making your server do work.

## Hash Tables


- **Hash tables have really fast search, insert, and delete.**
- Hash tables are good for modeling relationships from one
item to another item.
- Hash tables are used for caching data (for example, with
a web server).
- Hash tables are great for catching duplicates.

**Don't necessarily need to know:** 
- Once your load factor is greater than .07, it’s time to resize
your hash table.
- You can make a hash table by combining a hash function
with an array. 
- Collisions are bad. You need a hash function that
minimizes collisions. 

**Great Practical Use of Hash Tables**

See Chris' Explanation of NoSQL Global Secondary Index (Ruby):
```
users = {
  'userId1' => {
    'username' => 'user 1',
    'email' => 'email 1'
  },
  'userId2' => {
    'username' => 'user 2',
    'email' => 'email 2'
  }
}

p users['userId2']['username']
# > "user 2"

#Global Secondary Index
usersUsernames = {
  'user 1' => 'userId1',
  'user 2' => 'userId2'
}

p users[usersUsernames['user 2']]
# > {"username"=>"user 2", "email"=>"email 2"}
```

This makes use of Hash Tables' constant time to find data quickly.

## Chapter 6: Breadth-First Search


### What is a Graph?

Graphs are a way to model how different things are connected to one another.

A graph models a set of connections, made up of nodes and edges. A node can be directly connected to many other nodes. Those nodes are called its neighbors.

Graph of people who owe other people money:

    
    Alex -> Rama ---> Adit
              ^      ^
               \    /
                Tom

Alex owes Rama money, Tom owes Adit money, and so on. Each graph
is made up of *nodes* and *edges*.


    (node)
      |
      v
    Alex -----> Rama
          ^
          |
        (edge)

### Breadth-First Search

Can answer two types of questions:

1. Question type 1: **Is there a path** from node A to node B? (Is there a
mango seller in your network?)
2. Question type 2: What is the **shortest path** from node A to node B?
(Who is the closest mango seller?)

Bread-first search finds the shortest path by working from a **queue** (FIFO - First In First Out), as opposed to a stack (LIFO - Last In First Out). 

In the friend/mango seller example (where we are searching Facebook friends), we would prefer to find a seller in our first-degree connections over second, and second over third. Bread-first searches all first-degree connections before moving on to second - i.e. a QUEUE.

    if first_degree_connection == mango-seller
      return first_degree_connection
    else
      add_all__their_friends_to_queue()
      (...continue searching from first_degree_connection...)

Example with Route:

          Node -- Finish
         /           ^
    Start            |
         \           |
           Node -- Node

The shortest path has a length of 2. Bread-first search checks both nodes in first positions:

    Node == Finish? 
      Yes:
        return
      else:
        check_next_node()

### Implementing the Graph in Python:
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    print(graph)
    > {'you': ['alice', 'bob', 'claire']}
    print(graph["you"])
    > ['alice', 'bob', 'claire']

Notice that “you” is mapped to an array. So `graph[“you”]` will give you
an array of all the neighbors of “you”.

    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    
    print(graph)
    > {'you': ['alice', 'bob', 'claire'], 'bob': ['anuj', 'peggy'], 'alice': ['peggy'], 'claire': ['thom', 'jonny'], 'anuj': [], 'peggy': [], 'thom': [], 'jonny': []}

**Directed Graph:** One way relationship; edge 2->3 means can go from 2 to 3, that edge is directed;

"There is only an edge from 2 to 3 and no edge from 3 to 2. Therefore you can go from vertex 2 to vertex 3 but not from 3 to 2." - [stackoverflow](https://stackoverflow.com/questions/23956467/what-is-the-difference-between-a-directed-and-undirected-graph)

    e.g. Bob is Anuj's neighbour: `graph["bob"] = ["anuj", "peggy"]`
    but Bob is not Anuj's neighbour: `graph["anuj"] = []`

**Undirected Graph:** no arrows, both nodes are each other's neighbours;

"In undirected graph 2-3 means the edge has no direction, i.e. 2-3 means you can go both from 2 to 3 and 3 to 2." - (same Stackoverflow post).

### Implementing the Algorithm

Make a queue to start. In Python, you use the *double-ended queue*
(**deque**) function for this:

    from collections import deque
    search_queue = deque() 
    search_queue += graph[“you”]

    while search_queue:
        person = search_queue.popleft() #<- grabs the first person off the queue
        if person_is_seller(person):
            print person + “ is a mango seller!”
            return True
        else:
            search_queue += graph[person] #<- add all of this person's friend's to end of search_queue
    return False #<- noone in the queue was a mango seller

NOTE: You will need to keep a record of checked_people to avoid an infinite loop (i.e. same person could be in two people's friends lists - what if the code keeps adding them then friend then them &c.)

FINAL CODE:

    def person_is_seller(name):
        return name[-1] == 'y'


    def breadth_first_search(name):
        search_queue = deque()
        search_queue += graph[name]
        searched = []
        while search_queue:
            person = search_queue.popleft()
            if not person in searched:
                if person_is_seller(person):
                    print(person + " is a mango seller!")
                    return True
                else:
                    search_queue += graph[person]
                    searched.append(person)
        return False


    print(breadth_first_search("you"))
    > peggy is a mango seller!
    > True

### Running Time

O(V+E) - (V for number of vertices, E for number of edges). 

Breakdown in Mango seller example:

Follow each edge (i.e. connection between each person) = O(number of edges). 

Also keep a queue of every person to search and add to queue. Adding 1 person to queue takes constant time - O(1), so doing this for every person will take O(number of people) total.

Breadth-first search therefore takes O(number of people + number of edges), and it’s more commonly written as O(V+E) (V for number of vertices, E for number of edges).

**Tree:** a special type of graph, where no edges ever point back (like a family tree).

### Recap
- Breadth-first search tells you if there’s a path from A to B.
- If there’s a path, breadth-first search will find the shortest path.
- If you have a problem like “find the shortest X,” try modeling your problem as a graph, and use breadth-first search to solve.
- A directed graph has arrows, and the relationship follows the direction of the arrow (rama -> adit means “rama owes adit money”).
- Undirected graphs don’t have arrows, and the relationship goes both ways (ross - rachel means “ross dated rachel and rachel dated ross”).
- Queues are FIFO (First In, First Out).
- Stacks are LIFO (Last In, First Out).
- You need to check people in the order they were added to the search list, so the search list needs to be a queue. Otherwise, you won’t get the shortest path.
- Once you check someone, make sure you don’t check them again. Otherwise, you might end up in an infinite loop.

