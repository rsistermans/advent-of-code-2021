with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution(numbers):

    integers = []
    for line in numbers:
        integers.append([int(c) for c in line])

    numbers = integers

    max_x = len(numbers[0])
    max_y = len(numbers)

    basins = []
    for y in range(0, max_y):
        for x in range(0, max_x):
            top = 10
            bottom = 10
            left = 10
            right = 10
            if y > 0:
                top = numbers[y-1][x]
            if x > 0:
                left = numbers[y][x-1]
            if y < max_y - 1:
                bottom = numbers[y+1][x]
            if x < max_x - 1:
                right = numbers[y][x+1]
            number = numbers[y][x]
            if number < top and number < bottom and number < left and number < right:
                check_basin(x, y, number, numbers)
                count = 0
                for (ii, i) in enumerate(numbers):
                    for (ji, j) in enumerate(i):
                        if j == -1:
                            count += 1
                            numbers[ii][ji] = 9
                basins.append(count)

    basins.sort()
    largest_basins = basins[-3:]
    result = 1

    for i in largest_basins:
        result *= i

    print(result)


def check_basin(x, y, number, numbers):
    max_x = len(numbers[0])
    max_y = len(numbers)

    changed_coords = []

    for i in range(1, max_y):
        if y - i >= 0:
            value = numbers[y-i][x]
            if value < 9 and value != -1:
                changed_coords.append((x, y-i))
                numbers[y-i][x] = -1
            else:
                break

    for i in range(1, max_y):
        if y + i < max_y:
            value = numbers[y+i][x]
            if value < 9 and value != -1:
                changed_coords.append((x, y+i))
                numbers[y+i][x] = -1
            else:
                break

    for i in range(1, max_x):
        if x - i >= 0:
            value = numbers[y][x-i]
            if value < 9 and value != -1:
                changed_coords.append((x-i, y))
                numbers[y][x-i] = -1
            else:
                break

    for i in range(1, max_x):
        if x + i < max_x:
            value = numbers[y][x+i]
            if value < 9 and value != -1:
                changed_coords.append((x+i, y))
                numbers[y][x+i] = -1
            else:
                break

    for coord in changed_coords:
        x = coord[0]
        y = coord[1]
        check_basin(x, y, numbers[y][x], numbers)

    numbers[y][x] = -1


solution(lines)
