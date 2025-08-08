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

    for i in range(height // 2):
        for j in range(width // 2):
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


def move_pacman(direction, level):
    new_pos = [level.pacman_pos[0] + direction[0], level.pacman_pos[1] + direction[1]]

    # Check for collision with walls
    if (new_pos[0], new_pos[1]) not in level.walls:
        level.pacman_pos = new_pos


def move_ghost(level):
    direction = random.choice([UP, DOWN, LEFT, RIGHT])
    new_pos = [level.ghost_pos[0] + direction[0], level.ghost_pos[1] + direction[1]]

    # Ensure ghost stays inside the grid
    if (new_pos[0], new_pos[1]) not in level.walls:
        level.ghost_pos = new_pos


def check_collision(level):
    if level.pacman_pos == level.ghost_pos:
        return True
    return False


def check_pellet(level):
    if tuple(level.pacman_pos) in level.pellets:
        level.pellets.remove(tuple(level.pacman_pos))
        return True
    return False


def game_loop(stdscr, level):
    key = curses.KEY_RIGHT
    score = 0
    frame_rate = 0.1  # Set the frame rate to 10 frames per second (100 ms per frame)

    while True:
        start_time = time.time()  # Track the start of the frame

        draw_window(stdscr, level)

        # Check for user input
        key = stdscr.getch()

        if key == ord("q"):  # Quit the game
            break

        # Move Pac-Man based on input
        if key == curses.KEY_UP:
            move_pacman(UP, level)
        elif key == curses.KEY_DOWN:
            move_pacman(DOWN, level)
        elif key == curses.KEY_LEFT:
            move_pacman(LEFT, level)
        elif key == curses.KEY_RIGHT:
            move_pacman(RIGHT, level)

        # Check if Pac-Man eats a pellet
        if check_pellet(level):
            score += 10

        # Move the ghost
        move_ghost(level)

        # Check for collision with ghost
        if check_collision(level):
            stdscr.addstr(HEIGHT // 2, WIDTH // 2, "GAME OVER!", curses.A_BOLD)
            stdscr.refresh()
            time.sleep(2)
            break

        # Check if all pellets are eaten (victory condition)
        if len(level.pellets) == 0:
            stdscr.addstr(HEIGHT // 2, WIDTH // 2, "YOU WIN!", curses.A_BOLD)
            stdscr.refresh()
            time.sleep(2)
            break

        # Display score
        stdscr.addstr(0, WIDTH + 2, f"Score: {score}")

        # Calculate elapsed time for the frame
        elapsed_time = time.time() - start_time
        sleep_time = max(
            0, frame_rate - elapsed_time
        )  # Ensure we don't sleep for negative time

        # Sleep to maintain consistent frame rate
        time.sleep(sleep_time)

        stdscr.refresh()


def main(stdscr):
    # Initialize the window
    curses.use_default_colors()
    curses.curs_set(0)  # Hide cursor
    stdscr.timeout(100)  # Set timeout to make it responsive

    level = Level()

    game_loop(stdscr, level)
    return


# Run the game loop
curses.wrapper(main)
