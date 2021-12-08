with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


coord_map = {
    'T': None,
    'M': None,
    'B': None,
    'L1': None,
    'L2': None,
    'R1': None,
    'R2': None
}


def solution(lines):
    result = 0
    for line in lines:
        i, o = parse_line(line)
        digit_index = map_to_digit_index(i)
        digit_map = map_to_coords(digit_index)
        digit_map_keys = list(digit_map.keys())
        number_string = ''
        for i in o:
            i_sorted = "".join(sorted(i))
            key = list(filter(lambda x: "".join(sorted(x)) == i_sorted, digit_map_keys))[0]
            number_string += str(digit_map[key])
        result += int(number_string)
    print(result)


def parse_line(line):
    first = line.split(' |')[0].split(' ')
    last = line.split('| ')[1].split(' ')
    return first, last


def map_to_coords(di):
    result = coord_map.copy()

    di_keys = list(di.keys())
    di_values = list(di.values())

    d0 = ''
    d1 = di_keys[di_values.index(1)]
    d2 = ''
    d3 = ''
    d4 = di_keys[di_values.index(4)]
    d5 = ''
    d6 = ''
    d7 = di_keys[di_values.index(7)]
    d8 = di_keys[di_values.index(8)]
    d9 = ''

    result['T'] = [i for i in d7 if i not in d1][0]

    # find 9, as it contains all items from 4 plus two more
    d9_options = list(filter(lambda x: len(x) == 6, di_keys))
    for option in d9_options:
        if all((c in option) for c in d4):
            d9 = option
            di[option] = 9

    # difference between 9 and 8 is L2
    result['L2'] = [i for i in d8 if i not in d9][0]

    # I know 5 and 6 as they only differ by L2
    # filter all items that have L2 and length of 5
    d5_options = list(filter(lambda x: len(x) == 5 and result['L2'] not in x, di_keys))
    # filter all items that don't have L2 and length of 6
    d6_options = list(filter(lambda x: len(x) == 6 and result['L2'] in x, di_keys))
    # get the 2 options that only differ by 1 char
    for d5_option in d5_options:
        for d6_option in d6_options:
            # all d5 characters should be in d6
            intersection = [i for i in d5_option if i in d6_option]
            if len(intersection) == 5:
                d5 = d5_option
                di[d5] = 5
                d6 = d6_option
                di[d6] = 6
                break

    # we now know the other 5 length options
    d2_or_d3 = list(filter(lambda x: len(x) == 5, di_keys))

    # d2 is the one that has L2
    d2 = [i for i in d2_or_d3 if result['L2'] in i][0]
    di[d2] = 2

    # d3 is the one that doesn't have L2
    d3 = [i for i in d2_or_d3 if i != d2 and i != d5][0]
    di[d3] = 3

    d0 = list(filter(lambda x: di[x] is None, di_keys))[0]
    di[d0] = 0

    return di


def map_to_digit_index(segment):
    result = {}
    for i in segment:
        easy_digit = check_for_easy_digit(i)
        result[i] = easy_digit
    return result


def check_for_easy_digit(d):
    if len(d) == 2:
        return 1
    elif len(d) == 4:
        return 4
    elif len(d) == 3:
        return 7
    elif len(d) == 7:
        return 8


solution(lines)
