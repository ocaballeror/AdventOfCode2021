import itertools


class Grid:
    def __init__(self, data):
        self.grid = data
        self.flashes = 0

    def __getitem__(self, acc):
        x, y = acc
        return self.grid[y][x]

    def __setitem__(self, acc, value):
        x, y = acc
        self.grid[y][x] = value

    def iter_coords(self):
        for y, row in enumerate(self.grid):
            for x, _ in enumerate(row):
                yield x, y

    def iter_values(self):
        for coord in self.iter_coords():
            yield self[coord]

    def adjacent(self, point):
        x, y = point
        for movex, movey in [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]:
            if 0 <= x + movex < len(self.grid[0]) and 0 <= y + movey < len(
                self.grid
            ):
                yield x + movex, y + movey

    def explode(self):
        exploded = set()
        prev_count = -1
        while len(exploded) > prev_count:
            prev_count = len(exploded)

            for coord in self.iter_coords():
                if coord in exploded or self[coord] <= 9:
                    continue

                exploded.add(coord)
                self.flashes += 1
                for other in self.adjacent(coord):
                    self[other] += 1

        for coord in exploded:
            self[coord] = 0

    def step(self):
        for x, y in self.iter_coords():
            self[(x, y)] += 1

        self.explode()

    def draw(self):
        for line in self.grid:
            print("".join(map(str, line)))
        print("")


def read_input():
    with open("input") as f:
        content = f.read()

    lines = content.strip().split("\n")
    lines = [[int(c) for c in line] for line in lines]
    return Grid(lines)


def part1():
    grid = read_input()
    for _ in range(100):
        grid.step()

    return grid.flashes


def part2():
    grid = read_input()
    for step in itertools.count(1):
        grid.step()
        if all(octo == 0 for octo in grid.iter_values()):
            break

    return step


if __name__ == '__main__':
    print("Part 1", part1())
    print("Part 2", part2())
