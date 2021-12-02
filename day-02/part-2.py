with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution(lines):
    horizontal = 0
    depth = 0
    aim = 0

    for (i, n) in enumerate(lines):
        direction, value = n.split()
        if direction == "forward":
            horizontal += int(value)
            depth += (aim * int(value))
        elif direction == "down":
            aim += int(value)
        elif direction == "up":
            aim -= int(value)

    print(horizontal * depth)


solution(lines)
