with open('input.txt') as f:
    lines = [int(i) for i in f.readlines()[0].strip().split(',')]


def solution(numbers):

    numbers.sort()
    median = numbers.sort()[len(numbers) // 2]

    fuel = 0
    for n in numbers:
        fuel += abs(median - n)

    print(fuel)


solution(lines)
