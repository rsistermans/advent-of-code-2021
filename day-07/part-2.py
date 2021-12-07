with open('input.txt') as f:
    lines = [int(i) for i in f.readlines()[0].strip().split(',')]


def solution(numbers):

    max_pos = max(numbers)

    options = []

    for i in range(1, max_pos + 1):
        fuel = 0
        for n in numbers:
            dist = abs(n - i)
            fuel += sum(range(dist+1))
        options.append(fuel)

    print(min(options))


solution(lines)
