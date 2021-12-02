with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution(lines):
    horizontal = 0
    depth = 0
    aim = 0

    for (i, n) in enumerate(lines):
        chunks = n.split(" ")
        if chunks[0] == "forward":
            horizontal += int(chunks[1])
            depth += (aim * int(chunks[1]))
        elif chunks[0] == "down":
            aim += int(chunks[1])
        elif chunks[0] == "up":
            aim -= int(chunks[1])

    print(horizontal * depth)


solution(lines)
