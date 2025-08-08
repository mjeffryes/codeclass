import curses
import q

ROWS = 40
COL_WIDTH = 10


def init_color_support():
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)


def print_colors(screen):
    # Clear the screen
    screen.clear()
    init_color_support()
    # Get the number of colors available
    num_colors = curses.COLORS
    q(num_colors)
    # Print the number of colors
    screen.addstr(0, 0, f"Number of colors available: {num_colors}\n")
    # Print each color
    for i in range(num_colors):
        q(i)
        screen.addstr(
            i % ROWS + 1,
            (i // ROWS) * COL_WIDTH,
            f"Color {i} ",
            curses.color_pair(i),
        )
    # Refresh the screen to show changes
    screen.refresh()
    # Wait for user input before exiting
    screen.getch()


curses.wrapper(print_colors)
