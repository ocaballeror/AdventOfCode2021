import re
import itertools


def read_input():
    with open("input") as f:
        patt = r"x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)"
        xa, xb, ya, yb = map(int, re.search(patt, f.read().strip()).groups())
        return range(xa, xb), range(ya, yb)


def lands(x, y, xrange, yrange):
    velx = x
    vely = y

    while not (x in xrange and y in yrange):
        if x >= xrange.stop or y <= yrange.start:
            return False
        vely -= 1
        if velx > 0:
            velx -= 1
        y += vely
        x += velx

    return True


def part1():
    # The idea here is that we know that no matter which y velocity we choose,
    # the projectile will come back to 0 with the same initial velocity but
    # negative. if that velocity is higher than the distance from 0 to the far
    # edge of the target, we'll completely miss it, so in theory, the maximum y
    # we can chose is the lowest point of the target - 1.
    # Here we calculate the highest point we can reach with that initial y
    # velocity, which is the decreasing sum from y to 0
    xrange, yrange = read_input()
    return sum(i for i in range(-yrange.start))


def part2():
    xrange, yrange = read_input()

    # minimum x will be the smallest summatory that is in range
    minx = 0
    dist = 0
    while dist < xrange.start:
        minx += 1
        dist += minx

    maxx = xrange.stop
    maxy = -yrange.start
    miny = yrange.start

    # include the edges in the range
    xrange = range(xrange.start, xrange.stop+1)
    yrange = range(yrange.start, yrange.stop+1)

    # try all possible x, y combinations in the range
    candidates = itertools.product(range(minx, maxx+1), range(miny, maxy+1))
    return sum(lands(x, y, xrange, yrange) for x, y in candidates)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
