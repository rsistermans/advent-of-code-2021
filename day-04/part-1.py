with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution(lines):
    numbers = list(map(lambda x: int(x), lines[0].split(',')))
    bingo_cards = generate_bingo_cards(lines)

    winning_number = None
    validated_bingo_cards = []

    for n in numbers:
        bingo_cards = draw_number(n, bingo_cards)

        if n >= 4:
            validated_bingo_cards = validate_bingo_cards(bingo_cards)
            if len(validated_bingo_cards) > 0:
                winning_number = n
                break

    if validated_bingo_cards[0]:
        unmarked_numbers = get_unmarked_numbers(validated_bingo_cards[0])
        sum_of_numbers = 0
        for n in unmarked_numbers:
            sum_of_numbers += n

        print(sum_of_numbers * winning_number)


def generate_bingo_cards(lines):
    result = [[]]
    for (index, line) in enumerate(lines[2:]):
        if line != '':
            result[-1].append(list(map(lambda x: {int(x): False}, line.split())))
        else:
            result.append([])
    return result


def draw_number(number, bingo_cards):
    for card in bingo_cards:
        for line in card:
            for item in line:
                for key, value in item.items():
                    if key == number:
                        item.update({key: True})
    return bingo_cards


def validate_bingo_cards(bingo_cards):
    return list(filter(check_for_bingo, bingo_cards))


def check_for_bingo(bingo_card):
    # check for horizontal bingo
    for line in bingo_card:
        values = list(map(lambda x: list(x.values())[0], line))
        if all(values):
            return True

    # check for vertical bingo
    for i in range(5):
        vertical_line = []
        for line in bingo_card:
            vertical_line.append(line[i])
        values = list(map(lambda x: list(x.values())[0], vertical_line))
        if all(values):
            return True

    return False

def get_unmarked_numbers(bingo_card):
    unmarked_numbers = []
    for line in bingo_card:
        for item in line:
            key, value = list(item.items())[0]
            if not value:
                unmarked_numbers.append(key)
    return unmarked_numbers


solution(lines)
