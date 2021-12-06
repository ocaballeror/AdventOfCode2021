import itertools
from collections import Counter


def read_input(skip_diag=True):
    points = []
    with open("input") as f:
        for line in f:
            start, end = line.split(' -> ')
            x1, y1 = map(int, start.split(','))
            x2, y2 = map(int, end.split(','))
            if x1 != x2 and y1 != y2:
                if skip_diag:
                    continue
                if abs(x1 - x2) != abs(y1 - y2):
                    continue

            if x1 < x2:
                xrange = range(x1, x2+1)
            elif x1 > x2:
                xrange = range(x1, x2-1, -1)
            else:
                xrange = itertools.repeat(x1)
            if y1 < y2:
                yrange = range(y1, y2+1)
            elif y1 > y2:
                yrange = range(y1, y2-1, -1)
            else:
                yrange = itertools.repeat(y1)

            for x, y in zip(xrange, yrange):
                points.append((x, y))

    return points


def part1():
    points = read_input()
    return len([x for x in Counter(points).values() if x > 1])


def part2():
    points = read_input(skip_diag=False)
    return len([x for x in Counter(points).values() if x > 1])


if __name__ == '__main__':
    print("Part 1", part1())
    print("Part 2", part2())
