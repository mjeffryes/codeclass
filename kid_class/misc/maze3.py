import curses
from random import random, choice

# --- Constants ---
WALL_CHAR = "█"
SPACE_CHAR = " "
PLAYER_CHAR = "*"
PLAYER_COLOR = 125
GHOST_CHAR = "G"
GHOST_COLORS = [196, 202, 208, 214]


# --- Actor Class ---
class Actor:
    def __init__(self, char, color, x, y):
        self.char = char
        self.color = color
        self.x = x
        self.y = y

    def move(self, dx, dy, maze):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]):
            if maze[new_y][new_x] != WALL_CHAR:
                self.x = new_x
                self.y = new_y
                return True
        return False

    def draw(self, screen):
        screen.addstr(self.y, self.x, self.char, curses.color_pair(self.color))


# --- Maze Generation ---
def genMaze(height, width):
    maze = []
    for i in range(height):
        row = []
        for j in range(width):
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
    for i, row in enumerate(maze):
        for j, ch in enumerate(row):
            screen.addstr(i, j, ch)


def init_color_support():
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)


# --- Main App ---
def run_app(screen):
    init_color_support()
    screen.timeout(100)  # make game loop run ~10x per second
    max_y, max_x = screen.getmaxyx()
    maze = genMaze(max_y - 1, max_x - 1)

    # Create player
    player = Actor(PLAYER_CHAR, PLAYER_COLOR, 1, 1)

    # Create ghosts
    ghosts = []
    ghost_positions = [(10, 10), (15, 5), (20, 12), (25, 8)]
    for i in range(4):
        gx, gy = ghost_positions[i]
        ghosts.append(Actor(GHOST_CHAR, GHOST_COLORS[i], gx, gy))

    while True:
        screen.clear()
        printMaze(maze, screen)

        # Draw all actors
        player.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)

        screen.refresh()

        key = screen.getch()

        # Move player
        if key == curses.KEY_UP:
            player.move(0, -1, maze)
        elif key == curses.KEY_DOWN:
            player.move(0, 1, maze)
        elif key == curses.KEY_LEFT:
            player.move(-1, 0, maze)
        elif key == curses.KEY_RIGHT:
            player.move(1, 0, maze)
        elif key == ord("q"):
            break  # quit

        # Move ghosts randomly
        for ghost in ghosts:
            for _ in range(5):  # try 5 random directions until one works
                dx, dy = choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
                if ghost.move(dx, dy, maze):
                    break


curses.wrapper(run_app)
