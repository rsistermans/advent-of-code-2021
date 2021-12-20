with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution():

    target_area = get_target_area(lines[0])

    hits = []

    for x_res in range(1, max(target_area[0]) + 1):
        for y_res in range(-500, 500):
            x = 0
            y = 0
            x_velocity = x_res
            y_velocity = y_res
            max_y = y
            has_reached_target = False
            while not has_reached_target:
                max_y = max([y, max_y])
                x += x_velocity
                if x_velocity < 0:
                    x_velocity += 1
                elif x_velocity > 0:
                    x_velocity -= 1
                y += y_velocity
                y_velocity -= 1
                check = check_target(x, y, target_area)
                if check == 1:
                    hits.append({(x_res, y_res): max_y})
                    has_reached_target = True
                elif check == 2:
                    has_reached_target = True
    print(len(hits))


def check_target(x, y, target_area):
    # 0 = continue
    # 1 = hit
    # 2 = miss
    x_min = min(target_area[0])
    y_min = min(target_area[1])
    x_max = max(target_area[0])
    y_max = max(target_area[1])
    if x_min <= x <= x_max and y_min <= y <= y_max:
        return 1
    elif x > x_max or y < y_min:
        return 2
    return 0




def get_target_area(line):
    pieces = line.split("=")
    x = set([int(x) for x in pieces[1][:-3].split("..")])
    y = set([int(y) for y in pieces[2].split('..')])
    return x, y


solution()
