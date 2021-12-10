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
    scores = []
    for line in lines:
        FOUND = False
        openings = []
        for char in line:
            if FOUND == True:
                break
            else:
                if char in list(chars.keys()):
                    openings.append(char)
                else:
                    for (key, value) in chars.items():
                        if char == value:
                            if len(openings) > 0 and openings[-1] == key:
                                openings = openings[:-1]
                            else:
                                first_illegal_chars.append(value)
                                FOUND = True
        if len(openings) > 0 and FOUND == False:
            closings = []
            score = 0
            for opening in openings[::-1]:
                score *= 5
                closing = chars[opening]
                closings.append(closing)
                if closing == ')':
                    score += 1
                elif closing == ']':
                    score += 2
                elif closing == '}':
                    score += 3
                elif closing == '>':
                    score += 4
            scores.append(score)

    scores.sort()
    print(scores[len(scores) // 2])


solution(lines)
