# Experiments with Algorithms

Translating the algorithm examples in Aditya Bhargava's *Grokking Algorithms* from Python into Ruby to ensure I fully understand them. 

## Notes on Chapter 1

<!-- ### The first time I've ever wished I continued maths after year 11... ###
 -->


### Solidifying my Understanding of Exponentials and Intro to Logarithms

Exponentials: 

10<sup>2</sup> = 10 * 10 = 100

10<sup>3</sup> = 10 * 10 * 10 = 1000

10<sup>10</sup> = 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10  *or (10 * 10 ten times)* = 10bil

Logarithms: 

Expenentials flipped. 

10<sup>2</sup> = 100 <->log<sub>10</sub> 100= 2 (i.e. 10 * 10 = 100)

10<sup>3</sup> = 1000 <->log<sub>10</sub> 100= 2 (i.e. 10 * 10 = 100)

2<sup>3</sup> = 8 <->log<sub>2</sub> 8= 3 (i.e. 2 * 2 * 2 = 8)

When discussing Big O notation in the book log always means log<sub>2</sub> 

### Big O Notation 

Simple search = going throuhg list one by one. O(n) - i.e. the max number of times you have to iterate through the list is equal to the length the list. 

For list of 8 numbers, simple search = O(8)

Binary search = have to check max log n. 

For list of 8, binary = O(log<sub>3</sub>) i.e. 3 guesses max. 



