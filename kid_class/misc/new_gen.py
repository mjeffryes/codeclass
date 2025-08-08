import curses
import random
import time

# Define constants
WIDTH = 31
HEIGHT = 15
PACMAN = "P"
EMPTY = " "
WALL = "█"
PELLET = "."
GHOST = "G"

# Directions for movement
LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)


def generate_maze(width, height):
    DIRS = [LEFT, RIGHT, UP, DOWN]
    maze = [[WALL] * width for _ in range(height)]

    maze[1][1] = EMPTY

    # Function to perform DFS and carve the maze
    def dfs(x, y):
        # Shuffle directions to get random order
        random.shuffle(DIRS)

        for dx, dy in DIRS:
            nx, ny = x + (2 * dx), y + (2 * dy)

            # Check if the new position is inside the bounds of the maze
            if (
                1 <= nx <= height // 2
                and 1 <= ny <= width // 2
                and maze[nx][ny] == WALL
            ):
                # Carve a path to the new cell (open it and the wall between)
                maze[nx][ny] = EMPTY
                maze[x + dx][y + dy] = EMPTY  # Open the wall between
                dfs(nx, ny)  # Recursively call DFS on the new cell

    # Start DFS from the top-left corner
    dfs(1, 1)

    for i in range(height // 2 + 1):
        for j in range(width // 2 + 1):
            maze[-(i + 1)][j] = maze[i][-(j + 1)] = maze[-(i + 1)][-(j + 1)] = maze[i][
                j
            ]

    return maze


class Level:
    pacman_pos = [HEIGHT // 2, WIDTH // 2]
    ghost_pos = [random.randint(1, HEIGHT - 2), random.randint(1, WIDTH - 2)]
    pellets = [
        (random.randint(1, HEIGHT - 2), random.randint(1, WIDTH - 2)) for _ in range(10)
    ]
    walls = generate_maze(WIDTH, HEIGHT)


def draw_window(stdscr, level):
    # Draw the window border
    for y in range(HEIGHT):
        for x in range(WIDTH):
            stdscr.addstr(y, x, level.walls[y][x])
            if (y, x) in level.pellets:
                stdscr.addstr(y, x, PELLET)
            elif [y, x] == level.pacman_pos:
                stdscr.addstr(y, x, PACMAN)
            elif [y, x] == level.ghost_pos:
                stdscr.addstr(y, x, GHOST)
    stdscr.refresh()


def check_pellet(level):
    if tuple(level.pacman_pos) in level.pellets:
        level.pellets.remove(tuple(level.pacman_pos))
        return True
    return False


def main(stdscr):
    # Initialize the window
    curses.curs_set(0)  # Hide cursor
    curses.use_default_colors()
    level = Level()
    draw_window(stdscr, level)
    # Check for user input
    key = stdscr.getch()
    return


# Run the game loop
curses.wrapper(main)
