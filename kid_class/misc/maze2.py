import curses
from random import random

# --- Constants ---
WALL_CHAR = "\u2588"
SPACE_CHAR = " "
PLAYER_CHAR = "*"
PLAYER_COLOR = 125


# --- Actor Class ---
class Actor:
    def __init__(self, char, color, x, y):
        self.char = char
        self.color = color
        self.x = x
        self.y = y

    def move(self, dx, dy, max_x, max_y):
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
                row.append(WALL_CHAR)
            elif i % 2 == 1 and j % 2 == 1:
                row.append(WALL_CHAR)
            elif (i % 2 == 1 or j % 2 == 1) and random() > 0.8:
                row.append(WALL_CHAR)
            else:
                row.append(SPACE_CHAR)
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
    maze = genMaze(max_y - 1, max_x - 1)

    player = Actor(PLAYER_CHAR, PLAYER_COLOR, 1, 1)

    while True:
        screen.clear()
        printMaze(maze, screen)
        player.draw(screen)
        screen.refresh()

        key = screen.getch()

        if key == curses.KEY_UP:
            player.move(0, -1, max_x, max_y)
        elif key == curses.KEY_DOWN:
            player.move(0, 1, max_x, max_y)
        elif key == curses.KEY_LEFT:
            player.move(-1, 0, max_x, max_y)
        elif key == curses.KEY_RIGHT:
            player.move(1, 0, max_x, max_y)
        else:
            break


curses.wrapper(run_app)
