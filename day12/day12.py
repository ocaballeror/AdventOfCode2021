from collections import defaultdict


def read_input():
    nodes = defaultdict(list)
    with open("input") as f:
        for line in f:
            a, b = line.strip().split('-')
            nodes[a].append(b)
            nodes[b].append(a)

    return nodes


def part1():
    adj = read_input()
    pending = {('start',)}
    done = set()
    while pending:
        path = pending.pop()
        for move in adj[path[-1]]:
            if move[0].islower() and move in path:
                continue
            if move == 'end':
                done.add(path + (move,))
            else:
                pending.add(path + (move,))

    return len(done)


def part2():
    adj = read_input()
    pending = {('start',)}
    done = set()
    while pending:
        path = pending.pop()
        for move in adj[path[-1]]:
            if move == 'start':
                continue

            if move == 'end':
                done.add(path + (move,))
                continue

            if move[0].islower() and move in path:
                if any(path.count(x) > 1 for x in adj if x[0].islower()):
                    continue
            pending.add(path + (move,))

    return len(done)


if __name__ == "__main__":
    print("Part 1", part1())
    print("Part 2", part2())
