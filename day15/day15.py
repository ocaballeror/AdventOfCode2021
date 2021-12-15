import heapq


class Grid:
    def __init__(self, data):
        self.grid = data
        self.factor = 1

    def __getitem__(self, acc):
        x, y = acc
        if x < 0 or y < 0 or x > self.cols - 1  or y > self.rows - 1:
            raise IndexError("Coordinate out of bounds")

        val = self.grid[y % self.real_rows][x % self.real_cols]
        val += x // self.real_cols + y // self.real_rows
        if val >= 10:
            val -= 9
        return val

    def __contains__(self, acc):
        try:
            self[acc]
        except IndexError:
            return False

        return True

    @property
    def real_rows(self):
        return len(self.grid)

    @property
    def real_cols(self):
        return len(self.grid[0])

    @property
    def rows(self):
        return len(self.grid) * self.factor

    @property
    def cols(self):
        return len(self.grid[0]) * self.factor

    @property
    def end(self):
        return self.cols - 1, self.rows - 1

    def grow(self, factor):
        self.factor = factor

    def adjacent(self, point):
        x, y = point
        for movex, movey in [
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 0),
        ]:
            if (x + movex, y + movey) in self:
                yield x + movex, y + movey

    def draw(self):
        for y in range(self.rows):
            print("".join(map(str, (self[(x, y)] for x in range(self.cols)))))
        print("")


def read_input():
    with open("input") as f:
        return Grid([[int(c) for c in line.strip()] for line in f])



def dijkstra(grid):
    seen = set()
    pending = [(0, (0, 0))]
    pset = set(pending)  # set copy of `pending` for faster membership checks
    while pending:
        cost, node = heapq.heappop(pending)
        pset.remove((cost, node))
        if node == grid.end:
            return cost

        for move in grid.adjacent(node):
            if move in seen:
                continue
            new = (cost + grid[move], move)
            if new in pset:
                continue
            heapq.heappush(pending, new)
            pset.add(new)

        seen.add(node)

    return -1


def part1():
    grid = read_input()
    return dijkstra(grid)


def part2():
    grid = read_input()
    grid.grow(5)
    return dijkstra(grid)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
