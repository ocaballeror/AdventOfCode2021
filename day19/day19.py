import itertools
from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int

    def __add__(self, other):
        return Point(x=self.x + other.x, y=self.y + other.y, z=self.z + other.z)

    def __sub__(self, other):
        return Point(x=self.x - other.x, y=self.y - other.y, z=self.z - other.z)

    def __mul__(self, other):
        return Point(x=self.x * other.x, y=self.y * other.y, z=self.z * other.z)

    def __neg__(self):
        return Point(x=-self.x, y=-self.y, z=-self.z)

    def __repr__(self):
        return ",".join(map(str, self.as_tuple()))

    def __lt__(self, other):
        return self.as_tuple() < other.as_tuple()

    def as_tuple(self):
        return self.x, self.y, self.z


def read_input():
    scanners = []
    with open("input") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "scanner" in line:
                scanners.append([])
                continue
            scanners[-1].append(Point(*(map(int, line.split(",")))))

    return scanners


def flips():
    yield from [
        lambda p: Point(p.x, p.y, p.z),
        lambda p: Point(p.x, -p.y, -p.z),
        lambda p: Point(-p.x, -p.y, p.z),
        lambda p: Point(-p.x, p.y, -p.z),
        lambda p: Point(p.x, p.z, -p.y),
        lambda p: Point(p.x, -p.z, p.y),
        lambda p: Point(-p.x, -p.z, -p.y),
        lambda p: Point(-p.x, p.z, p.y),
        lambda p: Point(-p.y, -p.x, -p.z),
        lambda p: Point(-p.y, p.x, p.z),
        lambda p: Point(p.y, -p.x, p.z),
        lambda p: Point(p.y, p.x, -p.z),
        lambda p: Point(-p.y, -p.z, p.x),
        lambda p: Point(-p.y, p.z, -p.x),
        lambda p: Point(p.y, -p.z, -p.x),
        lambda p: Point(p.y, p.z, p.x),
        lambda p: Point(-p.z, -p.x, p.y),
        lambda p: Point(-p.z, p.x, -p.y),
        lambda p: Point(p.z, -p.x, -p.y),
        lambda p: Point(p.z, p.x, p.y),
        lambda p: Point(-p.z, -p.y, -p.x),
        lambda p: Point(-p.z, p.y, p.x),
        lambda p: Point(p.z, -p.y, p.x),
        lambda p: Point(p.z, p.y, -p.x),
    ]


def align(existing, other):
    for flip in flips():
        new = [flip(p) for p in other]
        dist = defaultdict(list)
        for a, b in itertools.product(existing, new):
            dist[a - b].append((a, b))

        best = max(dist, key=lambda x: len(dist[x]))
        merge = dist[best]
        if len(merge) >= 12:
            diff = merge[0][0] - merge[0][1]
            return flip, diff

    return None


def manhattan(one, other):
    diff = one - other
    return abs(diff.x) + abs(diff.y) + abs(diff.z)


def count(scanners):
    beacons = set(scanners[0])
    rem = [set(item) for item in scanners[1:]]
    distances = []
    while rem:
        print('remaining:', len(rem))
        for scanner in list(rem):
            res = align(beacons, scanner)
            if not res:
                continue

            # breakpoint()
            func, diff = res
            distances.append(diff)
            new = {func(x) + diff for x in scanner}
            assert len(new & beacons) >= 12, breakpoint()
            beacons.update(new)
            rem.remove(scanner)

    print("Part 1:", len(beacons))

    far = max(manhattan(one, other) for one, other in itertools.product(distances, repeat=2))
    print("Part 2:", far)


if __name__ == "__main__":
    count(read_input())
