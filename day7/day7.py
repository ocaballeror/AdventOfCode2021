crabs = list(map(int, open("input").read().split(",")))


def part1():
    return min(
        sum(abs(c - align) for c in crabs)
        for align in range(min(crabs), max(crabs) + 1)
    )


def part2():
    return min(
        sum(sum(range(1, abs(crab - align) + 1)) for crab in crabs)
        for align in range(min(crabs), max(crabs) + 1)
    )


if __name__ == '__main__':
    print("Part 1", part1())
    print("Part 2", part2())
