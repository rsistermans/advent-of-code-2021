with open('input.txt') as f:
    lines = [int(i) for i in f.readlines()[0].strip().split(',')]


def solution(numbers):

    average = sum(numbers) // len(numbers)

    fuel = 0
    for n in numbers:
        fuel += sum(range(abs(average - n) + 1))

    print(fuel)


solution(lines)
