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
