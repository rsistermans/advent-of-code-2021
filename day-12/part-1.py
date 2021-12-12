import datetime

with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]


def solution(input):

    start = datetime.datetime.now()

    connections = parse_input(input)

    paths = get_paths('start', ['start'], connections)

    print(len(paths))

    end = datetime.datetime.now()

    print("Execution time", (end-start).microseconds // 1000)



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


def get_paths(path, result, connections):

    # path = start,A,c,A
    split_path = path.split(",")[-1]

    branches = connections[split_path]

    # remove start
    result = [r for r in result if r != path]
    for branch in [b for b in branches if b != 'start']:
        # add start,A
        # add start,B
        # if branch is not in path if it's lowercase
        if not branch.islower() or branch not in path:
            new_path = "".join([path, ",", branch])
            result.append(new_path)
            # result = [start,A / start,B]
            if branch != 'end':
                result = get_paths(new_path, result, connections)

    return result


solution(lines)
