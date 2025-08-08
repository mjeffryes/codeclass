import random
from collections import deque

WALL = "█"
OPEN = " "
BUFFER = "."


def generate_chunk(size=4, wall_fraction=0.5):
    grid = [[OPEN for _ in range(size)] for _ in range(size)]

    queue = [(random.randint(0, size - 1), random.randint(0, size - 1))]

    for _ in range(int(size * size * wall_fraction)):
        i = random.randint(0, len(queue) - 1)
        (y, x) = queue.pop(i)
        grid[y][x] = WALL
        neighbors = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
        new_neighbors = [
            (ny, nx)
            for ny, nx in neighbors
            if 0 <= ny < size and 0 <= nx < size and grid[ny][nx] == OPEN
        ]
        queue.extend(new_neighbors)

    return grid


def generate_chunked_maze(width=32, height=32, chunk_size=4, wall_fraction=0.5):
    WALL = "█"
    OPEN = " "
    BUFFER = "."

    grid = [[OPEN for _ in range(width)] for _ in range(height)]

    chunks_x = width // chunk_size
    chunks_y = height // c:qhunk_size

    chunks = [(y, x) for x in range(chunks_x) for y in range(chunks_y)]

    random.shuffle(chunks)

    for cy, cx in chunks:
        chunk = generate_chunk(size=chunk_size - 1, wall_fraction=wall_fraction)
        for y in range(chunk_size - 1):
            for x in range(chunk_size - 1):
                tx = cx * chunk_size + x
                ty = cy * chunk_size + y
                if ty < height and tx < width:
                    if chunk[y][x] == WALL:
                        grid[ty][tx] = chunk[y][x]

    return grid


def print_maze(grid):
    for row in grid:
        print("".join(row))


# Example usage
if __name__ == "__main__":
    maze = generate_chunked_maze(width=32, height=32, chunk_size=4, wall_fraction=0.5)
    print_maze(maze)
