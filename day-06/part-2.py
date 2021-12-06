with open('input.txt') as f:
    lines = [int(i) for i in f.readlines()[0].strip().split(',')]


def solution(numbers):

    indices = {}
    for i in range(9):
        indices[i] = 0

    for n in numbers:
        indices[n] += 1

    for i in range(256):
        new_indices = dict(indices)
        new_indices[0] = indices[1]
        new_indices[1] = indices[2]
        new_indices[2] = indices[3]
        new_indices[3] = indices[4]
        new_indices[4] = indices[5]
        new_indices[5] = indices[6]
        new_indices[6] = indices[0] + indices[7]
        new_indices[7] = indices[8]
        new_indices[8] = indices[0]
        indices = new_indices

    print(sum(indices.values()))


solution(lines)
