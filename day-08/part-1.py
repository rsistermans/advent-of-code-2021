with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution(numbers):

    count = 0
    for l in lines:
        digits = l.split('| ')[1].split(' ')
        for d in digits:
            if len(d) == 2 or len(d) == 3 or len(d) == 4 or len(d) == 7:
                count += 1

    print(count)


solution(lines)
