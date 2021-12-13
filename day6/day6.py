from collections import Counter


def read_input():
    with open("input") as f:
        return list(map(int, f.read().strip().split(",")))


def calculate(total):
    fish = Counter({i: 0 for i in range(9)})
    fish.update(read_input())

    for day in range(total):
        pre = fish.copy()
        fish[0] = pre[1]
        fish[1] = pre[2]
        fish[2] = pre[3]
        fish[3] = pre[4]
        fish[4] = pre[5]
        fish[5] = pre[6]
        fish[6] = pre[7] + pre[0]
        fish[7] = pre[8]
        fish[8] = pre[0]

    return sum(fish.values())


def part1():
    return calculate(80)


def part2():
    return calculate(256)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
