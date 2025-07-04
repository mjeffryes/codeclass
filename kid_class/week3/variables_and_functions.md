# Variables and Functions

What makes computers so useful? You might boil it down to 2 things that computers are really good at: math and storing lots of information or instructions for later retrieval. Since computers can store so much information, a key challenge for working with them or programming them can be keeping track of what's stored where. Most programming languages have two key concepts for keeping track of information: Variables and Functions.

## Variables
Variables are a way of storing information in your program so you can use it later. You can think of them like a named box that can hold a piece of information, like a number, or a "character" (ie. letters like 'a', or 'f')), or even a list of numbers or characters (usually called a "string").  You put something in the box by "assigning" it to a name. In python we use the "=" sign for this:
```python
x = 10 # store the number 10 in variable 'x'
y = "a cat" # store the letters "a cat" in variable 'y'

variables_can_have_long_names_too = "wow"

# you can make lists of any value too
a_list_of_numbers = [1, 5, 2]
some_letters = ["c", "a", "t"]
list_of_lists = [[1, 2], [3, 4]]
```
Variable names can use letters, numbers and even some punctuation like `_` or `-`.
Once a variable is assigned a value, you can use that variable name anywhere in your program where you need a value eg:
```python
a = 10
b = 20
foo = a + b

print(foo) # 50

b = a + 2

print(b) # 12
print(foo) # 50 (still)
```
Variables make it possible to write programs that "keep track" of information you've given them to do something useful eg.
```python
# Prompt the user to enter their name and store it in 'name'
name = input("What is your name? ")

# we can now use `name` any time we want to retrieve what the user typed
if name == "Kirklan":
  print("Hello " + name)
else if name == "Matt":
  print("Ugh not you again!")
else:
  print("Welcome " + name)
```
We've used variables a bit in our programs already eg. in our `for` loops the letters 'i' and 'j' are just variables that get assigned a new number from the range each time through the loop:
```python
# print the numbers 1 to 9
for i in range(1, 10):
    print(i)

# we can use any variable name we want
for goober in range(1, 10)
    print(goober) # think: why doesn't 'print(i)' work here
```
## Functions
Small programs can often just have all the instructions listed out one after another, but writing the same instructions over and over again is tedious and computers are good at remembering things for us. So most programming languages also have functions which are kind of like named boxes that hold code rather than data. You can even name a function in a very similar way to naming a variable:
```python
# create a function named `plus_ten` that takes a number as input and
# returns the value of that number plus 10
plus_ten = lambda num : num + 10
```
But because functions are so useful, most languages have a special syntax for assigning them:
```python
# this function does exactly the same thing as the one above
def plus_ten(num):
    return num + 10
```
We can use the code stored in the function by "applying" the function. To do that we just use the name of the function followed by `()`:
```python
def plus_ten(num):
    return num + 10

number = 10
bigger_number = plus_ten(number)

# we've actually been applying functions since the first day!
print(bigger_number) # 20

# functions can have as many inputs or "parameters" as you want, even 0
def add_three(a, b, c):
    return a + b + c

def print_hello():
    print("hello!") # the code in a function only runs when you apply it

print(add_three(1,2,4)) # 7
print(add_three) # guess what this does!

print_hello() # hello!
print_hello() # hello!
print_hello() # hello!
```
While we've only looked at small examples so far, these tools will help us a lot as we build more complex programs
## Practice: moving around a maze
With functions and variables, we can start to build programs that a more like the games and apps you are used to using. We'll start by using a tool called `ncurses`
to let us draw to the whole screen at once instead of just one line at a time:

```python
import curses

def run_app(screen):
  while True:
    # Clear screen
    screen.clear()

    # Add a string to the screen
    screen.addstr(1, 1, "Hello, Curses!")

    # Refresh the screen to show the changes
    screen.refresh()

    # Wait for a key press
    key = screen.getch()

curses.wrapper(run_app)
```

Notice how our code is written as a function that we "hand off" to the curses framework to run.  We can use variables to keep track of where on the screen to print the message, and read the user's key presses in a loop so they can move the message around the screen!

```python
import curses

def run_app(screen):
  x = 1
  y = 1
  while True:
    # Clear screen
    screen.clear()

    # Add a string to the screen
    screen.addstr(y, x, "Hello, Curses!")

    # Refresh the screen to show the changes
    screen.refresh()

    # Wait for a key press
    key = screen.getch()

    #move the text when the user presses a key
    if key == curses.KEY_UP:
      y = y - 1
    elif key == curses.KEY_DOWN:
      y = y + 1
    elif key == curses.KEY_LEFT:
      x = x - 1
    elif key == curses.KEY_RIGHT:
      x = x + 1
    else:
      break

curses.wrapper(run_app)
```

You probably noticed that the program crashed when you tried to move off the screen! Let's read how big the screen is and loop around to the other side.
```python
import curses

def run_app(screen):
  (max_y, max_x) = screen.getmaxyx()
  x = 1
  y = 1
  while True:
    # Clear screen
    screen.clear()

    # Add a string to the screen
    screen.addstr(y, x, "Hello, Curses!")

    # Refresh the screen to show the changes
    screen.refresh()

    # Wait for a key press
    key = screen.getch()

    #move the text when the user presses a key
    if key == curses.KEY_UP:
      y = y - 1
    elif key == curses.KEY_DOWN:
      y = y + 1
    elif key == curses.KEY_LEFT:
      x = x - 1
    elif key == curses.KEY_RIGHT:
      x = x + 1
    else:
      break

    y = y % max_y
    x = x % max_x

curses.wrapper(run_app)
```

The `curses` framework also lets us change the colors of the text, lets make it a red `*`:

```python
import curses

def init_color_support():
  curses.start_color()
  curses.use_default_colors()
  for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, -1)

def run_app(screen):
  init_color_support()
  (max_y, max_x) = screen.getmaxyx()
  x = 1
  y = 1
  while True:
    # Clear screen
    screen.clear()

    # Add a string to the screen
    #screen.addstr(y, x, "Hello, Curses!")
    screen.addstr(y, x, "*", curses.color_pair(125))

    # Refresh the screen to show the changes
    screen.refresh()

    # Wait for a key press
    key = screen.getch()

    #move the text when the user presses a key
    if key == curses.KEY_UP:
      y = y - 1
    elif key == curses.KEY_DOWN:
      y = y + 1
    elif key == curses.KEY_LEFT:
      x = x - 1
    elif key == curses.KEY_RIGHT:
      x = x + 1
    else:
      break

    y = y % max_y
    x = x % max_x

curses.wrapper(run_app)
```

Now let's add our maze generation code from last week in some helper functions and print out the maze too:

```python
import curses
from random import random

def genMaze(height, width):
  maze = []
  for i in range(0, height):
    row = []
    for j in range(0, width):
      if i == 0 or i == height - 1 or j == 0 or j == width - 1:
        row.append("#")
      elif (i % 2 == 1 and j % 2 == 1):
        row.append("#")
      elif (i % 2 == 1 or j % 2 == 1) and random() > 0.7:
        row.append("#")
      else:
        row.append(" ")
    maze.append(row)

  return maze

def printMaze(maze, screen):
  for i in range(0, len(maze)):
    for j in range(0, len(maze[i])):
      screen.addstr(i, j, maze[i][j])

def init_color_support():
  curses.start_color()
  curses.use_default_colors()
  for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, -1)

def run_app(screen):
  init_color_support()
  (max_y, max_x) = screen.getmaxyx()
  x = 1
  y = 1
  maze = genMaze(max_y-1, max_x-1)
  while True:
    # Clear screen
    screen.clear()

    printMaze(maze, screen)

    # Add a string to the screen
    screen.addstr(y, x, "*", curses.color_pair(125))

    # Refresh the screen to show the changes
    screen.refresh()

    # Wait for a key press
    key = screen.getch()

    #move the text when the user presses a key
    if key == curses.KEY_UP:
      y = y - 1
    elif key == curses.KEY_DOWN:
      y = y + 1
    elif key == curses.KEY_LEFT:
      x = x - 1
    elif key == curses.KEY_RIGHT:
      x = x + 1
    else:
      break

    y = y % max_y
    x = x % max_x

curses.wrapper(run_app)
```

Now we have character that can move around your maze, but it's a little funny since it can just
run over the walls, can you think how to make it so you have to go around the walls?
What about adding an entrance and exit you have to try to navigate between?


