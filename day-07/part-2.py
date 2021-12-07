with open('input.txt') as f:
    lines = [int(i) for i in f.readlines()[0].strip().split(',')]


def solution(numbers):

    distance = get_closest_distance(numbers)

    fuel = 0
    for n in numbers:
        dist = abs(n - distance)
        fuel += sum(range(dist + 1))

    print(fuel)


def get_closest_distance(numbers):
    unique_numbers = list(set(numbers))
    max_pos = max(unique_numbers)
    min_pos = min(unique_numbers)
    indices = [i for i in range(min_pos, max_pos + 1)]

    distance_sums = []

    for i in indices:
        distance = 0
        for n in unique_numbers:
            distance += abs(n - i)
        distance_sums.append(distance)

    closest_distance = min(distance_sums)
    return distance_sums.index(closest_distance) + 1


solution(lines)
