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
                pair_count_copy[pair] -= count
                for new_pair in [pair[0] + char, char + pair[1]]:
                    pair_count_copy[new_pair] += count
        pair_count = pair_count_copy

    # count chars
    result = {}
    for pair, count in pair_count.items():
        if pair[0] not in result.keys():
            result[pair[0]] = 0
        result[pair[0]] += count

    result[template[-1]] += 1

    result = result.values()
    print(max(result)-min(result))


def parse(lines):
    insertions = [line for line in lines if '->' in line]
    result = {}
    for i in insertions:
        parts = i.split()
        result[parts[0]] = parts[-1]
    return result


solution(lines)
