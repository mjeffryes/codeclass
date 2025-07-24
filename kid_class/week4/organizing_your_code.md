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

Next, we can write
```python
player = Actor(PLAYER, YELLOW, 1, 1)
```
instead of `x = 1` and `y = 1` to start the player. Use
```python
player.draw(screen)
```
 in place of `screen.addstr` to draw the player and update the code to move the user to
 ```python
         # move the text when the user presses a key
        direction = None
        if key == curses.KEY_UP:
            direction = UP
        elif key == curses.KEY_DOWN:
            direction = DOWN
        elif key == curses.KEY_LEFT:
            direction = LEFT
        elif key == curses.KEY_RIGHT:
            direction = RIGHT
        elif key == ord("q") or key == KEY_ESC:
            break

        if direction:
            player.move(direction, maze)
```
Try running your code here to see that it still works the same as it did before.

While so far we've mostly just moved some of the code around, having the actor class makes it really easy for us to add 4 ghosts to the game board and move them around randomly.  Add the following just after you create the `player` character:
```python
 ghosts = []
    for color in [RED, CYAN, PINK, ORANGE]:
        gy, gx = (random.randint(1, height - 1), random.randint(1, width - 1))
        ghosts.append(Actor(GHOST, color, gx, gy))
```
And after `player.draw(screen)` add
 ```python
        # Move ghosts randomly (and redraw them)
        for ghost in ghosts:
            ghost.move(random.choice([UP, DOWN, LEFT, RIGHT]), maze)
            ghost.draw(screen)
```
Try running your code here to see the ghosts!

Now, it's a bit strange that the ghosts only move when we press a key, so our next step will be to let our game loop run independent of the user's input. Add the following to the top of `run_app`
```python
    screen.timeout(100)  # make game loop run ~10x per second
```
The `timeout` sets how long `getch()` waits for input. This allows the loop to continue even if no key is pressed, letting ghosts move on their own.

Since the user won't always have pressed a key, we'll need to change how we exit  the game. Replace the `else: break` at the end of `run_app` to
```python
           elif key == ord("q"):
            break
```
and put the call to player.move in an if statement:
```python
        if direction:
            player.move(direction, maze)
```
Now the game will only exit if we hit the 'q' key. Also we probably want to make sure the maze isn't too big, both to make the game easier to finish and to avodi flicker. Let's define two more constants at the top of the file:
```python
MAX_HEIGHT = 10
MAX_WIDTH = 20
```
and then limit the size of our maze to fit in the smaller of either our window or the limits we just set:
```python
	(height, width) = (min(max_y - 1, MAX_HEIGHT), min(max_x - 1, MAX_WIDTH))
	maze = genMaze(height, width)

	# also update how we create the ghosts
	ghosts = []
    for color in [RED, CYAN, PINK, ORANGE]:
        gy, gx = (random.randint(1, height - 1), random.randint(1, width - 1))
        ghosts.append(Actor(GHOST, color, gx, gy)
```
It's also getting to be a bit weird that everyone can move through the walls, lets have the `move` method of `Actor` class check if there's a wall in the way first. To do that we'll need to add a parameter with the maze walls. We can replace the `max_y` and `max_y` parameters since we'll get them from the maze itself. We'll also add a return value that indicates if the move was successful or not:
```python
    def move(self, direction, maze):
        max_y = len(maze)
        max_x = len(maze[0])
        (dy, dx) = direction
        new_x = (self.x + dx) % max_x
        new_y = (self.y + dy) % max_y
        if maze[new_y][new_x] != WALL:
            self.x = new_x
            self.y = new_y
            return True
        return False
```

After updating  `run_app` to call the new `move` method Now all the characters in the game obey the rule to not walk through walls! Here's the full program so far:

Next, we probably want to add pellets to the game for PacMan to eat. The pellets are part of the game map, so we'll start by moving the map into a class and add a set holding a pellet for each location on the map that's not a wall:
```python
class GameMap:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.maze = genMaze(height, width)
        self.pellets = []
        for y in range(0, height):
            for x in range(0, width):
                if self.maze[y][x] == SPACE:
                    self.pellets.append((y, x))

    def draw(self, screen):
        for i in range(0, self.height):
            for j in range(0, self.width):
                screen.addstr(i, j, self.maze[i][j])

        for y, x in self.pellets:
            screen.addstr(y, x, PELLET)

    def eatPellet(self, y, x):
        if (y, x) in self.pellets:
            self.pellets.remove((y, x))
            return True
```
Then we can update the run_app method to use this map class and let pacman eat the pellets.

Finally, add some win/lose conditions. When all the pellets are gone, the player wins, but if they hit a ghost, they lose:
```python
        # Check for collisions with ghosts
        if any(ghost.x == player.x and ghost.y == player.y for ghost in ghosts):
            screen.addstr(height // 2, width // 2 - 5, "Game Over!", curses.A_BOLD)
            screen.refresh()
            time.sleep(2)
            break

        # Check if all pellets are eaten
        if len(maze.pellets) == 0:
            screen.addstr(height // 2, width // 2 - 5, "You Win!", curses.A_BOLD)
            screen.refresh()
            time.sleep(2)
            break
```
Here's what we ended up:
``` python

import curses
import random
import time

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

# terminal colors
RED = 125
GREEN = 84
BLUE = 22
CYAN = 52
PINK = 208
PURPLE = 94
YELLOW = 228
ORANGE = 209

KEY_ESC = 27  # ASCII code for ESC key

MAX_HEIGHT = 10
MAX_WIDTH = 20


class Actor:
    def __init__(self, char, color, x, y):
        self.char = char
        self.color = color
        self.x = x
        self.y = y

    def move(self, direction, maze):
        (dy, dx) = direction
        new_x = (self.x + dx) % maze.width
        new_y = (self.y + dy) % maze.height
        if maze.maze[new_y][new_x] != WALL:
            self.x = new_x
            self.y = new_y
            return True
        return False

    def draw(self, screen):
        screen.addstr(self.y, self.x, self.char, curses.color_pair(self.color))


def genMaze(height, width):
    maze = []
    for i in range(0, height):
        row = []
        for j in range(0, width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                row.append(WALL)
            elif i % 2 == 1 and j % 2 == 1:
                row.append(WALL)
            elif (i % 2 == 1 or j % 2 == 1) and random.random() > 0.8:
                row.append(WALL)
            else:
                row.append(SPACE)
        maze.append(row)

    return maze


class GameMap:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.maze = genMaze(height, width)
        self.pellets = []
        for y in range(0, height):
            for x in range(0, width):
                if self.maze[y][x] == SPACE:
                    self.pellets.append((y, x))

    def draw(self, screen):
        for i in range(0, self.height):
            for j in range(0, self.width):
                screen.addstr(i, j, self.maze[i][j])

        for y, x in self.pellets:
            screen.addstr(y, x, PELLET)

    def eatPellet(self, y, x):
        if (y, x) in self.pellets:
            self.pellets.remove((y, x))
            return True


def init_color_support():
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)


def run_app(screen):
    screen.timeout(100)  # make game loop run ~10x per second
    init_color_support()

    (max_y, max_x) = screen.getmaxyx()
    (height, width) = (min(max_y - 1, MAX_HEIGHT), min(max_x - 1, MAX_WIDTH))
    maze = GameMap(height, width)

    player = Actor(PLAYER, YELLOW, 1, 1)
    ghosts = []
    for color in [RED, CYAN, PINK, ORANGE]:
        gy, gx = (random.randint(1, height - 1), random.randint(1, width - 1))
        ghosts.append(Actor(GHOST, color, gx, gy))

    while True:
        # Clear screen
        screen.clear()

        maze.draw(screen)

        # Draw the player
        player.draw(screen)

        # Move ghosts randomly (and redraw them)
        for ghost in ghosts:
            ghost.move(random.choice([UP, DOWN, LEFT, RIGHT]), maze)
            ghost.draw(screen)

        # Refresh the screen to show the changes
        screen.refresh()

        # Wait for a key press
        key = screen.getch()

        # move the text when the user presses a key
        direction = None
        if key == curses.KEY_UP:
            direction = UP
        elif key == curses.KEY_DOWN:
            direction = DOWN
        elif key == curses.KEY_LEFT:
            direction = LEFT
        elif key == curses.KEY_RIGHT:
            direction = RIGHT
        elif key == ord("q") or key == KEY_ESC:
            break

        if direction:
            player.move(direction, maze)

        maze.eatPellet(player.y, player.x)

        # Check for collisions with ghosts
        if any(ghost.x == player.x and ghost.y == player.y for ghost in ghosts):
            screen.addstr(height // 2, width // 2 - 5, "Game Over!", curses.A_BOLD)
            screen.refresh()
            time.sleep(2)
            break

        # Check if all pellets are eaten
        if len(maze.pellets) == 0:
            screen.addstr(height // 2, width // 2 - 5, "You Win!", curses.A_BOLD)
            screen.refresh()
            time.sleep(2)
            break


curses.wrapper(run_app)
```

Now we have a working game! There's lots you could do to extend it:
- Keep score
- Change how the maze is generated
- Add power ups that let you get extra points for catching the ghosts
- Let the player continue to new levels where the ghosts move faster

Happy Chomping!
