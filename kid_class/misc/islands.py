import random


def generate_island_map(width=20, height=10, num_islands=10, target_island_size=40):
    EMPTY = " "
    ISLAND_CHARS = "@ABCDEFGHIJ"  # Unique symbol per island (up to 11)
    BUFFER_CHARS = ".abcdefghij"  # Unique symbol per island (up to 11)

    grid = [[EMPTY for _ in range(width)] for _ in range(height)]

    def in_bounds(y, x):
        return 0 <= y < height and 0 <= x < width

    def mark_buffer_zone(y, x, char):
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                ny, nx = y + dy, x + dx
                if in_bounds(ny, nx) and grid[ny][nx] == EMPTY:
                    grid[ny][nx] = char

    # Step 1: Seed all islands
    seeds = []
    while len(seeds) < num_islands:
        y = random.randint(2, height - 3)
        x = random.randint(2, width - 3)
        island_id = len(seeds)
        seeds.append((island_id, y, x))
        print(f"Seeding island {island_id} at ({y}, {x})")
        grid[y][x] = ISLAND_CHARS[island_id]
        mark_buffer_zone(y, x, BUFFER_CHARS[island_id])

    # Step 2: Global randomized BFS
    queue = [(island_id, y, x) for (island_id, y, x) in seeds]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    j = 0
    while len(queue) > 0:  # and j < 1000:
        j += 1
        i = random.randint(0, len(queue) - 1)
        (island_id, y, x) = queue.pop(i)
        # print(f"Expanding island {island_id} at ({y}, {x})")
        grid[y][x] = ISLAND_CHARS[island_id]
        mark_buffer_zone(y, x, BUFFER_CHARS[island_id])

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            n2y, n2x = y + 2 * dy, x + 2 * dx
            if (
                in_bounds(ny, nx)
                and grid[ny][nx] == BUFFER_CHARS[island_id]
                and (not in_bounds(n2y, n2x) or grid[n2y][n2x] == EMPTY)
            ):
                queue.append((island_id, ny, nx))

    return grid


def print_map(grid):
    for row in grid:
        print("".join(row))


# Example run
if __name__ == "__main__":
    grid = generate_island_map(
        width=20, height=10, num_islands=10, target_island_size=40
    )
    print_map(grid)
