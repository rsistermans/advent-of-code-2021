with open('input.txt') as f:
    lines = f.readlines()


def solution(lines):
    numbers = [int(i.strip()) for i in lines]

    increased_measurements = 0

    for (i, n) in enumerate(numbers):
        if i > 0 and n > numbers[i-1]:
            increased_measurements += 1

    print(increased_measurements)


solution(lines)
