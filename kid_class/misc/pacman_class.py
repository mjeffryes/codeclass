import curses
import random

EMPTY = " "
WALL = "\u2588"


def genMaze(height, width):
    maze = []
    for i in range(0, height):
        row = []
        for j in range(0, width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                row.append(WALL)
            elif i % 2 == 1 and j % 2 == 1:
                row.append(WALL)
            elif (i % 2 == 1 or j % 2 == 1) and random.random() > 0.7:
                row.append(WALL)
            else:
                row.append(EMPTY)
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
        screen.clear()  # Clear screen
        curses.curs_set(0)  # Hide cursor

        printMaze(maze, screen)

        # Draw user character (in red) to the screen
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
