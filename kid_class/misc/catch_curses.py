import curses
import random
import time


def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(True)  # Don't block on getch
    stdscr.timeout(100)  # Refresh every 100 ms

    # Screen size
    sh, sw = stdscr.getmaxyx()

    # Basket setup
    basket_width = 5
    basket_y = sh - 2
    basket_x = sw // 2 - basket_width // 2

    # Falling object
    obj_x = random.randint(1, sw - 2)
    obj_y = 0

    score = 0

    while True:
        stdscr.clear()

        # Draw score
        stdscr.addstr(0, 2, f"Score: {score}")

        # Draw basket
        basket_str = "_" * basket_width
        stdscr.addstr(basket_y, basket_x, basket_str)

        # Draw falling object
        stdscr.addstr(obj_y, obj_x, "*")

        stdscr.refresh()

        # Handle input
        key = stdscr.getch()
        if key == curses.KEY_LEFT and basket_x > 0:
            basket_x -= 1
        elif key == curses.KEY_RIGHT and basket_x < sw - basket_width:
            basket_x += 1
        elif key == ord("q"):
            break

        # Move object
        obj_y += 1

        # Check for catch or miss
        if obj_y == basket_y:
            if basket_x <= obj_x < basket_x + basket_width:
                score += 1  # Caught it!
            # Reset object
            obj_y = 0
            obj_x = random.randint(1, sw - 2)

        # Game over if object reaches bottom (optional)
        if obj_y >= sh - 1:
            stdscr.addstr(sh // 2, sw // 2 - 5, "Game Over!")
            stdscr.refresh()
            time.sleep(2)
            break

        time.sleep(0.05)  # Slow down the loop slightly


curses.wrapper(main)
