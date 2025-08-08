import random

EMPTY = " "
WALL = "█"


def create_grid(width, height):
    return [[WALL for _ in range(width)] for _ in range(height)]


def carve_room(grid, x1, y1, x2, y2):
    raggedness = 0.1  # Adjust this value for more or less ragged edges
    for y in range(y1, y2):
        for x in range(x1, x2):
            if x == x1 or x == x2 - 1 or y == y1 or y == y2 - 1:
                # Edge: carve with some chance (adds bite)
                if random.random() < raggedness:
                    grid[y][x] = " "
            else:
                # Interior: mostly carve
                if True:  # random.random() > raggedness / 2:
                    grid[y][x] = " "


def bsp(grid, x, y, w, h, min_size):
    if w < min_size * 2 or h < min_size * 2:
        # Base case: carve out a room
        margin = 0
        room_x1 = x + margin
        room_y1 = y + margin
        room_x2 = x + w
        room_y2 = y + h
        carve_room(grid, room_x1, room_y1, room_x2, room_y2)
        return [(room_x1, room_y1, room_x2, room_y2)]

    horizontal = random.choice([True, False])
    if w > h:
        horizontal = False
    elif h > w:
        horizontal = True

    if horizontal:
        split = random.randint(y + min_size, y + h - min_size)
        top = bsp(grid, x, y, w, split - y, min_size)
        bottom = bsp(grid, x, split, w, y + h - split, min_size)
        # connect top and bottom
        # x_pos = random.randint(x + 1, x + w - 2)
        # grid[split][x_pos] = EMPTY
        return top + bottom
    else:
        split = random.randint(x + min_size, x + w - min_size)
        left = bsp(grid, x, y, split - x, h, min_size)
        right = bsp(grid, split, y, x + w - split, h, min_size)
        # connect left and right
        # y_pos = random.randint(y + 1, y + h - 2)
        # grid[y_pos][split] = EMPTY
        return left + right


def generate_bsp_maze(width, height, min_room_size=6):
    grid = create_grid(width, height)
    bsp(grid, 0, 0, width, height, min_room_size)
    return grid


# Example usage
if __name__ == "__main__":
    width, height = 60, 25
    maze = generate_bsp_maze(width, height, min_room_size=2)
    for row in maze:
        print("".join(row))
