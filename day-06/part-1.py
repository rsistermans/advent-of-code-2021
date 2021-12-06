import re

with open('example.txt') as f:
    lines = [int(i) for i in f.readlines()[0].strip().split(',')]


def solution(numbers):

    for i in range(80):
        numbers = cycle(numbers)

    print(len(numbers))


def cycle(numbers):
    new_numbers = []
    append_no = 0
    for n in numbers:
        if n == 0:
            new_numbers.append(6)
            append_no += 1
        else:
            new_numbers.append(n - 1)

    for i in range(append_no):
        new_numbers.append(8)
    return new_numbers




solution(lines)
