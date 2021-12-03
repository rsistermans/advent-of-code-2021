with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution(lines):

    oxygen_generator = get_oxygen_rating(lines)
    co2_scrubber = get_co2_scrubber_rating(lines)

    print(oxygen_generator * co2_scrubber)


def get_oxygen_rating(lines):
    i = 0
    while len(lines) > 1 and i < len(lines[0]):
        on = 0
        off = 0
        for (index, n) in enumerate(lines):
            if int(n[i]) == 1:
                on += 1
            else:
                off += 1
        bit = 1 if on >= off else 0
        lines = list(filter(lambda x: int(x[i]) == bit, lines))
        i += 1
    return int(lines[0], 2)

def get_co2_scrubber_rating(lines):
    i = 0
    while len(lines) > 1 and i < len(lines[0]):
        on = 0
        off = 0
        for (index, n) in enumerate(lines):
            if int(n[i]) == 1:
                on += 1
            else:
                off += 1
        bit = 1 if on >= off else 0
        lines = list(filter(lambda x: int(x[i]) == 1 - bit, lines))
        i += 1
    return int(lines[0], 2)


solution(lines)
