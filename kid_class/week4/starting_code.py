import curses
import random

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


def genMaze(height, width):
    maze = []
    for i in range(0, height):
        row = []
        for j in range(0, width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                row.append("#")
            elif i % 2 == 1 and j % 2 == 1:
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
    maze = genMaze(max_y - 1, max_x - 1)
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

        # move the text when the user presses a key
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
