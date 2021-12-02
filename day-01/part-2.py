with open('input.txt') as f:
    lines = f.readlines()


def solution(lines):
    numbers = [int(i.strip()) for i in lines]

    increased_measurements = 0

    for (i, n) in enumerate(numbers):
        if i >= 3:
            prev_sum = numbers[i-1] + numbers[i-2] + numbers[i-3]
            curr_sum = numbers[i] + numbers[i-1] + numbers[i-2]
            if curr_sum > prev_sum:
                increased_measurements += 1

    print(increased_measurements)


solution(lines)
