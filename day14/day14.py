from collections import Counter, defaultdict


def read_input():
    with open("input") as f:
        start = f.readline().strip()
        f.readline()  # empty line

        rules = {}
        for line in f:
            a, b = line.strip().split(" -> ")
            assert a not in rules
            rules[a] = b

    return start, rules


def simulate(times):
    state, rules = read_input()

    for t in range(times):
        newstate = [state[0]]
        for i in range(len(state) - 1):
            pair = state[i : i + 2]
            newstate.append(rules[pair[0] + pair[1]])
            newstate.append(pair[1])

        state = newstate

    count = Counter(state)
    return max(count.values()) - min(count.values())


def calculate(times):
    state, rules = read_input()

    # track the number of pairs of each type
    pairs = Counter([state[i : i + 2] for i in range(len(state) - 1)])

    for _ in range(times):
        # for each iteration, a single pair will increase the amount of the pairs it produces. e.g.:
        # AB
        #
        # AB -> C
        #
        # First iteration pairs: {"AB": 1}
        # Second iteration pairs: {"AC": 1, "CB": 1}

        new_pairs = defaultdict(int)
        for key, count in pairs.items():
            new_pairs[key[0] + rules[key]] += count
            new_pairs[rules[key] + key[1]] += count
        pairs = new_pairs

    # unfold the lists of pairs and count the real number of occurrences of each polymer
    polymers = set(x for k in pairs for x in k)
    counts = {pol: sum(v for k, v in pairs.items() if k[0] == pol) for pol in polymers}
    counts[state[-1]] += 1

    return max(counts.values()) - min(counts.values())


def part1():
    return simulate(10)


def part2():
    return calculate(40)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
