import random

WALL = "█"
PATH = " "


def generate_maze(width, height):
    grid = [[WALL for _ in range(width)] for _ in range(height)]

    def in_bounds(y, x):
        return 0 <= y < height and 0 <= x < width

    def carve_maze(y, x):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if in_bounds(ny, nx) and grid[ny][nx] == WALL:
                grid[ny][nx] = PATH
                grid[y + dy // 2][x + dx // 2] = PATH
                carve_maze(ny, nx)

    grid[0][0] = PATH
    carve_maze(0, 0)
    return grid


def remove_dead_ends(grid):
    height = len(grid)
    width = len(grid[0])

    def in_bounds(y, x):
        return 0 <= y < height and 0 <= x < width

    # 3. Remove all dead ends
    def is_dead_end(y, x):
        if grid[y][x] != PATH:
            return False
        neighbors = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
        return sum(1 for ny, nx in neighbors if grid[ny][nx] == PATH) == 1

    changed = True
    while changed:
        changed = False
        for y in range(1, height - 1):
            for x in range(1, width - 1):
                if is_dead_end(y, x):
                    # Turn dead end into wall and try to make an extra connection
                    grid[y][x] = WALL
                    # Try opening a nearby wall to connect it
                    for dy, dx in random.sample([(0, 1), (1, 0), (0, -1), (-1, 0)], 4):
                        ny, nx = y + dy, x + dx
                        if in_bounds(ny, nx) and grid[ny][nx] == WALL:
                            grid[ny][nx] = PATH
                            grid[y][x] = PATH
                            changed = True
                            break
    return grid


def generate_no_dead_end_maze(width=31, height=21):
    grid = [[WALL for _ in range(width)] for _ in range(height)]

    def in_bounds(y, x):
        return 0 <= y < height and 0 <= x < width

    maze = generate_maze(width // 2, height // 2)

    maze = remove_dead_ends(maze)

    for i in range(height // 2):
        for j in range(width // 2):
            # grid[i+1][j+1] = grid[-(i + 1)][j] = grid[i][-(j + 1)] = grid[-(i + 1)][ -(j + 1) ] = maze[i][j]
            grid[i + 1][j + 1] = maze[i][j]
        # grid[i + 1][-(j + 2)] = maze[i][j]
        # grid[-(i + 2)][j + 1] = maze[i][j]
        # grid[-(i + 2)][-(j + 2)] = maze[i][j]

    return grid


def print_maze(grid):
    for row in grid:
        print("".join(row))


# Example
if __name__ == "__main__":
    maze = generate_no_dead_end_maze(31, 21)
    print_maze(maze)
