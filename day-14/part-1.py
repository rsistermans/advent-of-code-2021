with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]

def solution(input):

    template = input[0]
    rules = parse(lines)

    for i in range(10):

        mutable_template = [char for char in template]

        for (index, char) in enumerate(reversed(mutable_template)):
            i = len(template) - index - 1
            if i != 0:
                prev_char = template[i-1]
                ins = rules[prev_char + char]
                mutable_template = mutable_template[:i] + [ins] + mutable_template[i:]

        template = "".join(mutable_template)
    print(template)
    quantities = count_quantities(template)
    count_max = max(quantities.values())
    count_min = min(quantities.values())
    print(count_max - count_min)


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
