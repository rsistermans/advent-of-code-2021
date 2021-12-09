with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution(numbers):

    integers = []
    for line in numbers:
        integers.append([int(c) for c in line])

    numbers = integers

    max_x = len(numbers[0])
    max_y = len(numbers)

    low_numbers = []
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
                low_numbers.append(number)

    print(sum(low_numbers) + len(low_numbers))


solution(lines)
