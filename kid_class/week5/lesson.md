# Creating Packages and Modules

In real-world Python projects, writing everything in one file quickly becomes messy. **Modules** and **packages** help us:

* Organize related functionality into separate files

* Reuse code across projects

* Make our code cleaner and easier to test

## Concepts

* A **module** is just a `.py` file with functions, classes, or variables.

* A **package** is a folder with an `__init__.py` file and one or more modules.

## Warm-Up: Create a Simple Utility Module

Python makes it easy to organize your code into reusable modules

1. Create a new file `math_utils.py`
2. Add a function:

   ```python
   def clamp(value, min_value, max_value):
       """Return the value clamped between min_value and max_value."""
       return max(min_value, min(value, max_value))
   ```
3. Use it in another file:

   ```python
   from math_utils import clamp

   print(clamp(15, 0, 10))  # Output: 10
   ```

This pattern — writing a function in one file and importing it in another — is the foundation of modular code.
Next, Let’s apply this to our Pac-Man-style game by extracting reusable logic into a package called `curses_game`.

## Step 1: Create the `curses_game` Package

We’ll extract only general-purpose logic into a reusable terminal game package called `curses_game`:
```
curses_game/
├── __init__.py
├── actors.py
├── constants.py
├── utils.py
```

First, create the folder `curses_game` by running `mkdir curses_game` in your terminal.
Then, create an empty `__init__.py` file by running `touch curses_game/__init__.py` in your terminal.
Finally, create each of the module files as shown below. (You can copy this code from your pacman game from last lesson.)

### `constants.py`

```python
# Game characters
WALL = "█"
SPACE = " "

# Directions
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

# Colors
RED = 125
GREEN = 84
BLUE = 22
CYAN = 52
PINK = 208
PURPLE = 94
YELLOW = 228
ORANGE = 209

KEY_ESC = 27
```

### `actors.py`

```python
import curses
from .constants import WALL

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
```

### `utils.py`

```python
import curses
import time

def init_color_support():
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

class GameArea:
    def __init__(self, screen, max_height, max_width):
        self.screen = screen
        (max_y, max_x) = screen.getmaxyx()
        self.height = min(max_y - 1, max_height)
        self.width = min(max_x - 1, max_width)

    def display_message(self, message):
        length = len(message)
        self.screen.addstr(self.height // 2, (self.width - length) // 2, message, curses.A_BOLD)
        self.screen.refresh()
        time.sleep(2)
```


## Step 2: Modify the Pac-Man Game to Use the Package

We can now simplify our pacman game by importing the functions and classes from our package.

### New `pacman.py`

```python
import curses
import random
from curses_game.constants import *
from curses_game.actors import Actor
from curses_game.utils import init_color_support, GameArea

# Game characters
PELLET = "."
PLAYER = "P"
GHOST = "G"

MAX_HEIGHT = 10
MAX_WIDTH = 20

def genMaze(height, width):
    maze = []
    for i in range(height):
        row = []
        for j in range(width):
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
        self.pellets = [(y, x) for y in range(height) for x in range(width) if self.maze[y][x] == SPACE]

    def draw(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                screen.addstr(y, x, self.maze[y][x])
        for y, x in self.pellets:
            screen.addstr(y, x, PELLET)

    def eatPellet(self, y, x):
        if (y, x) in self.pellets:
            self.pellets.remove((y, x))
            return True

def run_app(screen):
    screen.timeout(100)
    init_color_support()

    game_area = GameArea(screen, MAX_HEIGHT, MAX_WIDTH)
    (height, width) = (game_area.height, game_area.width)
    maze = GameMap(height, width)

    player = Actor(PLAYER, YELLOW, 1, 1)
    ghosts = [Actor(GHOST, color, random.randint(1, height - 2), random.randint(1, width - 2)) for color in [RED, CYAN, PINK, ORANGE]]

    while True:
        screen.clear()
        maze.draw(screen)
        player.draw(screen)

        for ghost in ghosts:
            ghost.move(random.choice([UP, DOWN, LEFT, RIGHT]), maze)
            ghost.draw(screen)

        screen.refresh()

        key = screen.getch()
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
        else:
            direction = None

        if direction:
            player.move(direction, maze)

        maze.eatPellet(player.y, player.x)

        if any(ghost.x == player.x and ghost.y == player.y for ghost in ghosts):
            game_area.display_message("Game Over!")
            break

        if len(maze.pellets) == 0:
            game_area.display_message("You Win!")
            break

curses.wrapper(run_app)
```

## Step 3: Create a New Game – Mini Space Invaders

This will reuse `Actor`, `GameMap`, and constants from our package.

### `space_invaders.py`

```python
import curses
import random
from curses_game.constants import *
from curses_game.actors import Actor
from curses_game.utils import init_color_support, GameArea

MAX_HEIGHT = 20
MAX_WIDTH = 60

# game characters
SHIP = "A"
ENEMY = "W"
BULLET = "|"


def run_space_invaders(screen):
    screen.timeout(100)
    init_color_support()

    game_area = GameArea(screen, MAX_HEIGHT, MAX_WIDTH)
    (max_y, max_x) = screen.getmaxyx()
    player = Actor(SHIP, GREEN, game_area.width // 2, game_area.height - 1)
    bullets = []
    enemies = [Actor(ENEMY, RED, x, 1) for x in range(5, game_area.width - 5, 4)]

    while True:
        screen.clear()

        for bullet in bullets[:]:
            bullet.y -= 1
            if bullet.y <= 0:
                bullets.remove(bullet)
            else:
                bullet.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)

        player.draw(screen)
        screen.refresh()

        key = screen.getch()
        if key == curses.KEY_LEFT:
            player.x = max(1, player.x - 1)
        elif key == curses.KEY_RIGHT:
            player.x = min(game_area.width - 1, player.x + 1)
        elif key == ord(" "):
            bullets.append(Actor(BULLET, YELLOW, player.x, player.y - 1))
        elif key == ord("q") or key == KEY_ESC:
            break

        # Collision check
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.x == enemy.x and bullet.y == enemy.y:
                    bullets.remove(bullet)
                    enemies.remove(enemy)

        if not enemies:
            game_area.display_message("You Win!")
            break

curses.wrapper(run_space_invaders)
```

Now you have created a small package that you can use to make games in your terminal! Here
are some suggestions for how you could keep building:
1. Add a `Score` class to the package and show score on screen
2. Add sound effects using `beep` or `winsound` (platform dependent)
3. Create a third game (e.g. Snake or Asteroids) using `curses_game`

