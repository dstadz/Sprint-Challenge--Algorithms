# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
LINEAR: while len arr is cubic, its going through at quadratic speed which boils down to (n^3/n^2 => n)

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
N LOG(N): the for in contributes to a linear time, while the while loop contributes the log(n) time (because of the j*=2)
```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
LINEAR: its only doing one operation per iteration, 1:1, ie linear

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

  current = n//2
  check if current is too high or not:
    if too high: current = current//2
    if too low: current = half way between current and top
    repeat until no more possible floors above or below
O(n) = log(n)
by cutting the possible floors in half everytime, we achieve log(n)