with open('input.txt') as f:
    lines = [[int(j) for j in i if j != '\n'] for i in f.readlines()]

max_y = len(lines)
max_x = len(lines[0])

flashes = 0
found = False
step = 0


def solution(grid):

    steps = 999999
    for i in range(steps):
        global step
        step = i+1
        if found:
            break
        grid = increase(grid)

    global flashes
    print(flashes)


def increase(grid):
    new_grid = [i[:] for i in grid]

    for y in range(max_y):
        for x in range(max_x):
            new_grid[y][x] += 1

    for y in range(max_y):
        for x in range(max_x):
            if new_grid[y][x] == 10:
                infect_neighbors(new_grid, y, x)

    number_of_flashes = 0
    for y in range(max_y):
        for x in range(max_x):
            if new_grid[y][x] == -1:
                new_grid[y][x] = 0
                number_of_flashes += 1
                global flashes
                flashes += 1

    if number_of_flashes == max_x * max_y:
        print("Number of flashes reached!")
        global found
        found = True
        print("step number", step)

    return new_grid


def infect_neighbors(grid, y, x):
    grid[y][x] = -1
    for n in [-1, 0, 1]:
        for m in [-1, 0, 1]:
            if not (n == 0 and m == 0):
                if 0 <= y+n < max_y and 0 <= x+m < max_x:
                    if grid[y+n][x+m] != -1 and grid[y+n][x+m] <= 9:
                        grid[y+n][x+m] += 1
                        if grid[y+n][x+m] > 9:
                            infect_neighbors(grid, y+n, x+m)


solution(lines)
