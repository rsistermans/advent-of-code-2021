with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution(input):

    grid, instructions = parse_input(input)

    for instruction in instructions:
        grid = fold(grid, instruction)

    result = 0
    for (y, line) in enumerate(grid):
        for (x, char) in enumerate(line):
            result += char
            if char == 0:
                grid[y][x] = ' '
            else:
                grid[y][x] = 'x'
    for line in grid:
        print(line)


def parse_input(lines):
    instructions = [(line.split()[-1].split('=')[0], int(line.split()[-1].split('=')[1])) for line in lines if line.startswith("fold")]
    max_x = next(x for x in instructions if x[0] == 'x')[1] * 2 + 1
    max_y = next(x for x in instructions if x[0] == 'y')[1] * 2 + 1

    coords = [[0] * max_x for _ in range(max_y)]
    fill = [line for line in lines if ',' in line]

    for line in fill:
        x, y = [int(x) for x in line.split(',')]
        coords[y][x] = 1

    return coords, instructions


def fold(grid, instruction):
    grid_copy = [x[:] for x in grid]
    if instruction[0] == 'y':
        # fold vertical
        fold1 = grid_copy[:instruction[1]]
        fold2 = grid_copy[instruction[1]+1:]
        if len(fold1) != len(fold2):
            print("ERROR!", len(fold1), len(fold2))
        # vertical mirror fold2
        fold2_copy = [x[:] for x in fold2]
        for (y, line) in enumerate(fold2):
            for (x, char) in enumerate(line):
                fold2_copy[-y-1][x] = char
        # merge fold1 with fold2
        fold1_copy = [x[:] for x in fold1]
        for (y, line) in enumerate(fold1):
            for (x, char) in enumerate(line):
                fold1_copy[y][x] = max([fold1[y][x], fold2_copy[y][x]])
        return fold1_copy

    elif instruction[0] == 'x':
        # fold horizontal
        fold1 = list(map(lambda x: x[:instruction[1]], grid))
        fold2 = list(map(lambda x: x[instruction[1]+1:], grid))
        # horizontal mirror fold2
        fold2_copy = [x[:] for x in fold2]
        for (y, line) in enumerate(fold2):
            for (x, char) in enumerate(line):
                fold2_copy[y][-x-1] = char
        # merge fold1 with fold2
        fold1_copy = [x[:] for x in fold1]
        for (y, line) in enumerate(fold1):
            for (x, char) in enumerate(line):
                fold1_copy[y][x] = max([fold1[y][x], fold2_copy[y][x]])
        return fold1_copy


solution(lines)