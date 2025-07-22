# Organizing your code 


As your programs grow in size and complexity, keeping your code organized becomes crucial. Organized code is easier to read, debug, and extend. In this lesson, we’ll look at how constants, classes, and modular structure help keep our code clean and understandable.

## Constants

Using constants is a good way to avoid hard-coded values scattered throughout your code. (These are sometimes called "magic numbers"!) If you use a specific character for a wall or a number to signify a key or a color, it’s better to define that at the top of your file. This way, if you need to change it, you only have to update it in one place.
### Example:
```python
# maze pieces
WALL = "█" # you can use "\u2588" if you can't type █! 
SPACE = " "
PELLET = "."
PLAYER = "P"
GHOST = "G"

# directions
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

# terminal colors
RED = 125
GREEN = 84
BLUE = 22
CYAN = 52
PINK = 208
PURPLE = 94
YELLOW = 228
ORANGE = 209
```
## Classes

Classes are a way to group together data (variables) and behaviors (functions) that belong together. This is especially helpful in games, where you often have multiple things (players, enemies, pellets, maps) that each have their own data and actions.
### Example:
```python
class Actor:
    def __init__(self, char, color, x, y):
        self.char = char
        self.color = color
        self.x = x
        self.y = y

    def move(self, direction, max_x, max_y):
	    (dy, dx) = direction
        self.x = (self.x + dx) % max_x
        self.y = (self.y + dy) % max_y

    def draw(self, screen):
        screen.addstr(self.y, self.x, self.char, curses.color_pair(self.color))
         ```

This "Actor" class can be used to represent a moving object in a curses game. The class holds 4 pieces of data: the character it's represented by on the screen, the color it's printed in, and the coordinates of where it is on screen. It has two  methods (functions attached to a class are usually called methods): one to move the actor one step on the board, and another to print the actor's character to the screen. 
## Exercise: PacMan

To practice organizing our code we'll start building a pac-man type game. As the program gets more complex, with enemies, pellets, keeping score, and possibly multiple levels, we'll want to use classes to organize related functions and data together.

Last time we ended class with a program that generates a maze with a character to move around in it:
```python
import curses
import random

def genMaze(height, width):
  maze = []
  for i in range(0, height):
    row = []
    for j in range(0, width):
      if i == 0 or i == height - 1 or j == 0 or j == width - 1:
        row.append("#")
      elif (i % 2 == 1 and j % 2 == 1):
        row.append("#")
      elif (i % 2 == 1 or j % 2 == 1) and random.random() > 0.8:
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

As a first step add the constants and `Actor` class at the top of your program so we can use them to simplify our code. Replace the hardcoded `"#"` and `" "` strings you used for the walls with the `WALL` and `SPACE` constants.

Next, we can write `player = Actor(PLAYER, YELLOW, 1, 1)` instead of `x = 1` and `y = 1` and call `player.draw(screen)` in place of `screen.addstr` and `player.move(UP, max_x, max_y)`

When you're done your code should look something like this:
```python
import curses
import random

# --- Constants ---
# maze pieces
WALL = "█" # you can use "\u2588" if you can't type █! 
SPACE = " "
PELLET = "."
PLAYER = "P"
GHOST = "G"

# directions
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

# terminal colors
RED = 125
GREEN = 84
BLUE = 22
CYAN = 52
PINK = 208
PURPLE = 94
YELLOW = 228
ORANGE = 209

# --- Actor Class ---
class Actor:
    def __init__(self, char, color, x, y):
        self.char = char
        self.color = color
        self.x = x
        self.y = y

    def move(self, direction, max_x, max_y):
	    (dy, dx) = direction
        self.x = (self.x + dx) % max_x
        self.y = (self.y + dy) % max_y

    def draw(self, screen):
        screen.addstr(self.y, self.x, self.char, curses.color_pair(self.color))

# --- Maze Generation ---
def genMaze(height, width):
    maze = []
    for i in range(0, height):
        row = []
        for j in range(0, width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                row.append(WALL)
            elif (i % 2 == 1 and j % 2 == 1):
                row.append(WALL)
            elif (i % 2 == 1 or j % 2 == 1) and random.random() > 0.8:
                row.append(WALL)
            else:
                row.append(SPACE)
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

# --- Main App ---
def run_app(screen):
    init_color_support()
    max_y, max_x = screen.getmaxyx()
    maze = genMaze(max

player.draw(screen)

    while True:
        screen.clear()
        printMaze(maze, screen)
        player.draw(screen)
        screen.refresh()

        key = screen.getch()

        if key == curses.KEY_UP:
            player.move(UP, max_x, max_y)
        elif key == curses.KEY_DOWN:
            player.move(DOWN, max_x, max_y)
        elif key == curses.KEY_LEFT:
            player.move(LEFT, max_x, max_y)
        elif key == curses.KEY_RIGHT:
            player.move(RIGHT, max_x, max_y)
        else:
            break

curses.wrapper(run_app)
```
While so far we've mostly just moved some of the code around, having the actor class makes it really easy for us to add 4 ghosts to the game board and move them around randomly.  Add the following just after you create the `player` character:
```python
    # Create ghosts
    ghosts = []
    for color in [RED, CYAN, PINK, ORANGE]:
        gx, gy = (random.randomint(max_y), random.randomint(max_x))
        ghosts.append(Actor(GHOST, color, gx, gy))
```
And after the if statements for the player key presses add
 ```python
        # move ghosts
        for ghost in ghosts:
			dx, dy = random.choice([LEFT, RIGHT, UP, DOWN])
			ghost.move(dx, dy, max_x, max_y):
```
Your code should now looks something like this:
```python
import curses
import random

# --- Constants ---
# maze pieces
WALL = "█"  # you can use "\u2588" if you can't type █!
SPACE = " "
PELLET = "."
PLAYER = "P"
GHOST = "G"

# directions
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

# terminal colors
RED = 125
GREEN = 84
BLUE = 22
CYAN = 52
PINK = 208
PURPLE = 94
YELLOW = 228
ORANGE = 209

# --- Actor Class ---
class Actor:
    def __init__(self, char, color, x, y):
        self.char = char
        self.color = color
        self.x = x
        self.y = y

    def move(self, direction, max_x, max_y):
        dy, dx = direction
        self.x = (self.x + dx) % max_x
        self.y = (self.y + dy) % max_y

    def draw(self, screen):
        screen.addstr(self.y, self.x, self.char, curses.color_pair(self.color))

# --- Maze Functions ---
def genMaze(height, width):
    maze = []
    for i in range(0, height):
        row = []
        for j in range(0, width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                row.append(WALL)
            elif (i % 2 == 1 and j % 2 == 1):
                row.append(WALL)
            elif (i % 2 == 1 or j % 2 == 1) and random.random() > 0.8:
                row.append(WALL)
            else:
                row.append(SPACE)
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

# --- Main Application ---
def run_app(screen):
    init_color_support()
    max_y, max_x = screen.getmaxyx()
    maze = genMaze(max_y - 1, max_x - 1)

    # Create player
    player = Actor(PLAYER, YELLOW, 1, 1)

    # Create ghosts
    ghosts = []
    for color in [RED, CYAN, PINK, ORANGE]:
        gx = random.randint(1, max_x - 2)
        gy = random.randint(1, max_y - 2)
        ghosts.append(Actor(GHOST, color, gx, gy))

    while True:
        screen.clear()
        printMaze(maze, screen)

        # Draw player and ghosts
        player.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)

        screen.refresh()

        key = screen.getch()
        if key == curses.KEY_UP:
            player.move(UP, max_x, max_y)
        elif key == curses.KEY_DOWN:
            player.move(DOWN, max_x, max_y)
        elif key == curses.KEY_LEFT:
            player.move(LEFT, max_x, max_y)
        elif key == curses.KEY_RIGHT:
            player.move(RIGHT, max_x, max_y)
        else:
            break

        # Move ghosts randomly
        for ghost in ghosts:
            direction = random.choice(DIRECTIONS)
            ghost.move(direction, max_x, max_y)

curses.wrapper(run_app)
```

Now it's a bit strange that the ghosts only move when we press a key, so our next step will be to let our game loop run independent of the user's input. Add the following to the top of `run_app`
```python
    screen.timeout(100)  # make game loop run ~10x per second
```

The `timeout` sets how long `getch()` waits for input. This allows the loop to continue even if no key is pressed, letting ghosts move on their own.

It's also getting to be a bit weird that everyone can move through the walls, lets have the `move` method of `Actor` class check if there's a wall in the way first. To do that we'll need to add a parameter with the maze walls. We can replace the `max_y` and `max_y` parameters since we'll get them from the maze itself. We'll also add a return value that indicates if the move was successful or not:
```python
    def move(self, direction, maze):
        max_y = len(maze)
        max_x = len(maze[0])
        (dy, dx) = direction
        new_x = (self.x + dx) % max_x
        new_y = (self.y + dy) % max_y
        if maze[new_y][new_x] != WALL_CHAR:
            self.x = new_x
            self.y = new_y
            return True
        return False
```
Now all the characters in the game obey the rule to not walk through walls! Here's the full program so far:

```python
import curses
import random

# --- Constants ---
# maze pieces
WALL = "█"  # or use "\u2588"
SPACE = " "
PELLET = "."
PLAYER = "P"
GHOST = "G"

# directions
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

# terminal colors
RED = 125
GREEN = 84
BLUE = 22
CYAN = 52
PINK = 208
PURPLE = 94
YELLOW = 228
ORANGE = 209

# --- Actor Class ---
class Actor:
    def __init__(self, char, color, x, y):
        self.char = char
        self.color = color
        self.x = x
        self.y = y

    def move(self, direction, maze):
        max_y = len(maze)
        max_x = len(maze[0])
        dy, dx = direction
        new_x = (self.x + dx) % max_x
        new_y = (self.y + dy) % max_y
        if maze[new_y][new_x] != WALL:
            self.x = new_x
            self.y = new_y
            return True
        return False

    def draw(self, screen):
        screen.addstr(self.y, self.x, self.char, curses.color_pair(self.color))

# --- Maze Functions ---
def genMaze(height, width):
    maze = []
    for i in range(height):
        row = []
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                row.append(WALL)
            elif (i % 2 == 1 and j % 2 == 1):
                row.append(WALL)
            elif (i % 2 == 1 or j % 2 == 1) and random.random() > 0.8:
                row.append(WALL)
            else:
                row.append(SPACE)
        maze.append(row)
    return maze

def printMaze(maze, screen):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            screen.addstr(i, j, maze[i][j])

def init_color_support():
    curses.start_color()
    curses.use_default_colors()
    for i in range(curses.COLORS):
        curses.init_pair(i + 1, i, -1)

# --- Main Application ---
def run_app(screen):
    init_color_support()
    screen.timeout(100)  # make game loop run ~10x per second

    max_y, max_x = screen.getmaxyx()
    maze = genMaze(max_y - 1, max_x - 1)

    # Create player
    player = Actor(PLAYER, YELLOW, 1, 1)

    # Create ghosts
    ghosts = []
    for color in [RED, CYAN, PINK, ORANGE]:
        while True:
            gx = random.randint(1, max_x - 2)
            gy = random.randint(1, max_y - 2)
            if maze[gy][gx] != WALL:
                break
        ghosts.append(Actor(GHOST, color, gx, gy))

    while True:
        screen.clear()
        printMaze(maze, screen)

        # Draw player and ghosts
        player.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)

        screen.refresh()

        key = screen.getch()
        if key == curses.KEY_UP:
            player.move(UP, maze)
        elif key == curses.KEY_DOWN:
            player.move(DOWN, maze)
        elif key == curses.KEY_LEFT:
            player.move(LEFT, maze)
        elif key == curses.KEY_RIGHT:
            player.move(RIGHT, maze)
        elif key == ord('q') or key == 27:  # ESC or 'q' to quit
            break

        # Move ghosts randomly
        for ghost in ghosts:
            direction = random.choice(DIRECTIONS)
            ghost.move(direction, maze)

curses.wrapper(run_app)
```
