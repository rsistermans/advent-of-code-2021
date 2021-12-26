import copy

with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution():
    grid = parse_input(lines)
    has_movement = True
    steps = 0
    while has_movement:
        grid, has_movement = cycle(grid)
        steps += 1
    print(steps)


def cycle(grid):
    max_y = len(grid)
    max_x = len(grid[0])
    new_grid = copy.deepcopy(grid)
    has_movement = False

    for (y, line) in enumerate(grid):
        for (x, cucumber) in enumerate(line):
            if cucumber == '>':
                right = x + 1 if x < max_x-1 else 0
                if grid[y][right] == '.':
                    new_grid[y][right] = '>'
                    new_grid[y][x] = '.'
                    has_movement = True

    grid = copy.deepcopy(new_grid)

    for (y, line) in enumerate(grid):
        for (x, cucumber) in enumerate(line):
            if cucumber == 'v':
                down = y + 1 if y < max_y-1 else 0
                if grid[down][x] == '.':
                    new_grid[down][x] = grid[y][x]
                    new_grid[y][x] = '.'
                    has_movement = True

    return new_grid, has_movement


def parse_input(lines):
    return [[c for c in line] for line in lines]


solution()
