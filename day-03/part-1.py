with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution(lines):
    gamma_rate = ''
    epsilon_rate = ''

    for i in range(len(lines[0])):
        on = 0
        off = 0
        for n in lines:
            if int(n[i]) == 1:
                on += 1
            else:
                off += 1
        gamma_rate += '1' if on > off else '0'
        epsilon_rate += '0' if on > off else '1'

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))


solution(lines)
