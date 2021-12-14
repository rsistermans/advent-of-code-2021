with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution(input):

    template = input[0]
    rules = parse(lines)

    pair_count = {}
    for rule in rules:
        pair_count[rule] = 0

    for i, c in enumerate(template):
        if i < len(template) - 1:
            pair = c + template[i+1]
            if pair not in pair_count.keys():
                pair_count[pair] = 1
            else:
                pair_count[pair] += 1

    for i in range(40):
        pair_count_copy = pair_count.copy()
        for pair, count in pair_count.items():
            if count > 0:
                char = rules[pair]
                new_pair_1 = pair[0] + char
                new_pair_2 = char + pair[1]
                pair_count_copy[pair] = pair_count_copy[pair] - count
                pair_count_copy[new_pair_1] = pair_count_copy[new_pair_1] + count
                pair_count_copy[new_pair_2] = pair_count_copy[new_pair_2] + count
        pair_count = pair_count_copy

    # count chars
    result = {}
    for pair, count in pair_count.items():
        if pair[0] not in result.keys():
            result[pair[0]] = 0
        result[pair[0]] += count

    result[template[-1]] += 1

    result_min = min(result.values())
    result_max = max(result.values())

    print(result_max - result_min)


def parse(lines):
    insertions = [line for line in lines if '->' in line]
    result = {}
    for i in insertions:
        parts = i.split()
        result[parts[0]] = parts[-1]
    return result


def count_quantities(string):
    result = {}
    for char in string:
        if char not in result.keys():
            result[char] = string.count(char)
    return result


solution(lines)
