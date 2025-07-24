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
