import re

with open('input.txt') as f:
    lines = [[int(j) for j in re.findall(r"[\w']+", i)] for i in f.readlines()]


def solution(lines):
    grid = create_grid(lines)
    for i in lines:
        fill_grid(grid, i)

    print(count_overlap(grid))


def create_grid(lines):
    max_x = max(list(map(lambda x: x[0], lines)) + list(map(lambda x: x[2], lines)))
    max_y = max(list(map(lambda x: x[1], lines)) + list(map(lambda x: x[3], lines)))
    return [[0 for _ in range(max_y + 1)] for _ in range(max_x + 1)]


def fill_grid(grid, line):
    if line[1] == line[3] and line[0] != line[2]:
        min_x = min(line[0], line[2])
        max_x = max(line[0], line[2])
        for i in range(min_x, max_x + 1):
            grid[i][line[3]] += 1
    elif line[0] == line[2] and line[1] != line[3]:
        min_y = min(line[1], line[3])
        max_y = max(line[1], line[3])
        for i in range(min_y, max_y + 1):
            grid[line[2]][i] += 1


def count_overlap(grid):
    flat_list = [item for line in grid for item in line]
    return sum(map(lambda x: x >= 2, flat_list))


solution(lines)
