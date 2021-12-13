with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution(input):

    grid, instructions = parse_input(input)

    for instruction in instructions[:1]:
        grid = fold(grid, instruction)

    result = 0
    for line in grid:
        for char in line:
            result += char
    print(result)


def parse_input(lines):
    max_x = max([int(line.split(',')[0]) for line in lines if "," in line])
    max_y = max([int(line.split(',')[1]) for line in lines if "," in line])
    instructions = []
    switch = False
    coords = [[0]*(max_x+1) for _ in range(max_y+1)]
    for line in lines:
        if line == '':
            switch = True
            continue
        if not switch:
            x, y = [int(x) for x in line.split(',')]
            coords[y][x] = 1
        else:
            instruction = line.split("=")
            instructions.append((instruction[0][-1], int(instruction[1])))
    return coords, instructions


def fold(grid, instruction):
    grid_copy = [x[:] for x in grid]
    if instruction[0] == 'y':
        # fold vertical
        fold1 = grid_copy[:instruction[1]]
        fold2 = grid_copy[instruction[1]+1:]
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
