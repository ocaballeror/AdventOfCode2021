from functools import reduce


def read_input():
    with open("input") as f:
        content = f.read()

    lines = content.strip().split("\n")
    lines = [[int(c) for c in line] for line in lines]
    return lines


def adjacent(point, cave):
    x, y = point
    for movex, movey in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        if 0 <= x + movex < len(cave[0]) and 0 <= y + movey < len(cave):
            yield x + movex, y + movey


def lows(cave):
    for y, row in enumerate(cave):
        for x, point in enumerate(row):
            if all(
                cave[othery][otherx] > point
                for otherx, othery in adjacent((x, y), cave)
            ):
                yield x, y


def part1():
    cave = read_input()
    return sum(cave[lowy][lowx] + 1 for lowx, lowy in lows(cave))


def part2():
    cave = read_input()
    basins = []

    for lowx, lowy in lows(cave):
        seen = set()
        pending = {(lowx, lowy)}

        while pending:
            pointx, pointy = pending.pop()
            for move in adjacent((pointx, pointy), cave):
                movex, movey = move
                if cave[movey][movex] == 9 or move in pending or move in seen:
                    continue
                pending.add((movex, movey))
            seen.add((pointx, pointy))

        basins.append(len(seen))

    best = sorted(basins, reverse=True)[:3]
    return reduce(lambda acc, n: acc * n, best, 1)


if __name__ == '__main__':
    print("Part 1", part1())
    print("Part 2", part2())
