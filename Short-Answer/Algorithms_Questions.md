# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0 #o(1)
    while (a < n * n * n): #o(n)
      a = a + n * n #o(1)
```


```
b)  sum = 0 o(1)
    for i in range(n): o(n)
      j = 1 o(1)
      while j < n:
        j *= 2
        sum += 1
```
o(1) + o(n) * (o(1) * o(n) * (o(1) +o(1))
o(1) + o(n) *(o(1) + o(2n))
o(1) + o(n) + o(2n^2)

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

n story building 

broken egg > f 
survives < f

starting from the bottom floor of the building i would drop an egg on each floor until the egg breaks to determine which floor the egg will break on 
-for each floor in the building 
-drop the egg 
=if the egg breaks return count of f 

because this function is iterating through the list of floors it would be 
0(n)

