with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution(lines):

    chars = {
        '{': '}',
        '[': ']',
        '(': ')',
        '<': '>'
    }

    first_illegal_chars = []
    for line in lines:
        FOUND = False
        openings = []
        for char in line:
            if FOUND == True:
                break
            else:
                if char in list(chars.keys()):
                    openings.append(char)
                    print(openings)
                else:
                    for (key, value) in chars.items():
                        if char == value:
                            if len(openings) > 0 and openings[-1] == key:
                                openings = openings[:-1]
                            else:
                                first_illegal_chars.append(value)
                                FOUND = True

    score = 0
    for char in first_illegal_chars:
        if char == ')':
            score += 3
        elif char == ']':
            score += 57
        elif char == '}':
            score += 1197
        elif char == '>':
            score += 25137

    print(score)


solution(lines)
