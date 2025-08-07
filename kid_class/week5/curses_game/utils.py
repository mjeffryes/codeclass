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
