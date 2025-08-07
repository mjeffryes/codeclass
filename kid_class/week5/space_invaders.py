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
