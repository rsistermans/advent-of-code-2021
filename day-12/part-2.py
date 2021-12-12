with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution(input):

    connections = parse_input(input)

    paths = get_paths('start', False, ['start'], connections)

    print(len(paths))


def parse_input(lines):
    connections = {}
    for line in lines:
        con1, con2 = line.split("-")
        if con1 not in connections.keys():
            connections[con1] = [con2]
        else:
            connections[con1].append(con2)
        if con2 not in connections.keys():
            connections[con2] = [con1]
        else:
            connections[con2].append(con1)
    return connections


def get_paths(path, has_double, result, connections):

    # path = start,A,c,A
    split_path = path.split(",")[-1]

    branches = connections[split_path]

    # remove start
    result = [r for r in result if r != path]
    for branch in [b for b in branches if b != 'start']:
        # add start,A
        # add start,B
        # if branch is not in path if it's lowercase
        if branch.islower():
            if path.count(branch) == 0:
                new_path = "".join([path, ",", branch])
                result.append(new_path)
                # result = [start,A / start,B]
                if branch != 'end':
                    result = get_paths(new_path, has_double, result, connections)
            elif path.count(branch) == 1:
                if not has_double:
                    # only do it once
                    new_path = "".join([path, ",", branch])
                    result.append(new_path)
                    # result = [start,A / start,B]
                    if branch != 'end':
                        result = get_paths(new_path, True, result, connections)
        else:
            new_path = "".join([path, ",", branch])
            result.append(new_path)
            # result = [start,A / start,B]
            if branch != 'end':
                result = get_paths(new_path, has_double, result, connections)

    return result


solution(lines)
