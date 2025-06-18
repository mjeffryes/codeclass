Loops and Conditionals
In order to build more complex programs, we need to be able to "steer" the computer through different parts of our code so we can do different things in different situations. Our most basic tools for doing this are loops and conditionals.

## Loops 
Loops tell the computer repeat a set of instructions.
Let's start with a simple loop that prints the same thing multiple times:
```python
for i in range(1, 10):
  print("#", end="")
```
(In python the whitespace matters, indenting the `print` line is what tells python that it should treat that code as part of the loop!)

We can nest loops inside other loops too!
```python
for i in range(1, 10):
  for j in range(1, 20):
    print("#", end="")
  print("")
```
# If-else
A "conditional" statement tells the computer to take different actions depending on the value of some "condition". The most essential conditional statement is an "if" statement:
```python
if 1 == 1:
	print("one does in fact equal one")
```
(We use a double equals sign when we're asking the computer "are these things equal?" You can also test for inequality with `!=` or compare which is bigger `>`, `<`, `<=`, `>=`)

An `if` statement is often paired with an `else`, telling the computer what to do if the condition is *not* true:
```python
if 1 == 2:
	print("Wat?")
else:
	print("one does not equal 2")
```
We can add an if-else to our program to tell it just to print "#" around the border:
```python
for i in range(1, 10):
  for j in range(1, 20):
    if i == 1 or i == 9 or j == 1 or j == 19:
      print("#", end="")
    else:
      print(" ", end="")
	  
  print("")
```
(Notice the `or` keyword lets us combine some conditions together, you can also use `and` to say that both conditions must be true or `not` to say the condition should not be true)
### elif
Sometimes you want more than two options. We could nest another `if` inside the `else` of our first `if` statements, but this is such a common need that python gives us a special keyword `elif` to take up less space:
```python
for i in range(1, 10):
  for j in range(1, 20):
    if i == 1 or i == 9 or j == 1 or j == 19:
      print("#", end="")
    elif (i % 2 == 1 or j % 2 == 1) :
      print("+", end="")
    else:
      print(" ", end="")
      
  print("")
```
(What's that `%` doing? It's called the "mod" or "modulus" operator. It divides the first number by the second one and returns the remainder. It's very often used for checking if a number is even or odd -  just like we're doing here!)
## "Maze" generator
With loops and conditionals we could construct arbitrarily complex designs, but we'd like to be able to make a new maze each time. Python can generate random numbers for us so we can start to make our design look like a maze:
```python
from random import random

for i in range(1, 10):
  for j in range(1, 20):
    if i == 1 or i == 9 or j == 1 or j == 19:
      print("#", end="")
    elif (i % 2 == 1 and j % 2 == 1):
      print("+", end="")
    elif (i % 2 == 1 or j % 2 == 1) and random() > 0.7:
      print("+", end="")
    else:
      print(" ", end="")

  print("")
```
(`random()` always returns a number between 0 and 1. Any number in that range is equally likely, so the condition we wrote will be true about 3/10 times and false about 7/10 times.)

So there you go! We now have something that generates maze-like patterns. It's not guaranteed to connect all the way through though because we're just picking walls to create at random. (We'll learn a bit later in the class how to make a maze that always connects!)

I'll leave you with a variation on our maze program that adds some more conditions and introduces "variables" which we'll talk about more next time we meet:
```python
from random import random

last_row = ["+"] * 20
for i in range(1, 10):
  for j in range(1, 20):
    threshold = 0.5
    if last_row[j] == "+":
      threshold = threshold + 0.2
    if last_row[j-1] == "+":
      threshold = threshold + 0.2

    if i == 1 or i == 9 or j == 1 or j == 19:
      print("#", end="")
    elif (i % 2 == 1 and j % 2 == 1):
      print("+", end="")
    elif (i % 2 == 1 or j % 2 == 1) and random() > threshold:
      print("+", end="")
      last_row[j] = "+"
    else:
      print(" ", end="")
      last_row[j] = " "

  print("")
```
(We've added two variables `threshold` and `last_row`. `last_row` holds a copy of one row's worth of symbols we've written in for the walls. We're looking at what we wrote just above and just to the left of us and increasing the value of `theshold` if it was a wall. We then compare our random number to `threshold` to decide whether to write a wall. The effect is that we're less likely to write a wall the more walls w)
