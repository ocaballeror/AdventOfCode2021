def read_input():
    lines = []
    with open("input") as f:
        for line in f:
            inp, outp = line.strip().split(" | ")
            lines.append((inp.split(), outp.split()))

    return lines


def part1():
    return sum(
        len([word for word in outp if len(word) in (2, 3, 4, 7)])
        for inp, outp in read_input()
    )


def reveal(inp):
    index = [""] * 10

    for w in inp:
        if len(w) == 2:
            index[1] = w
        elif len(w) == 3:
            index[7] = w
        elif len(w) == 4:
            index[4] = w
        elif len(w) == 7:
            index[8] = w

    # 3 is 7 with another two digits
    index[3] = next(
        w
        for w in inp
        if set(w).issuperset(index[7]) and len(w) == len(index[7]) + 2
    )

    # 9 is the union of 4 and 7 plus another digit
    union = set(index[4]).union(index[7])
    index[9] = next(
        w
        for w in inp
        if len(w) == 6 and len(set(w).symmetric_difference(union)) == 1
    )

    # 6 is the other 6 digit number that contains 9 minus 1
    index[6] = next(
        w
        for w in inp
        if len(w) == 6
        and w not in index
        and set(w).issuperset(set(index[9]).difference(index[1]))
    )

    # 0 is the remaining 6 digit
    index[0] = next(w for w in inp if len(w) == 6 and w not in index)

    # 5 is the 5digit that contains all of 9 minus 1
    index[5] = next(
        w
        for w in inp
        if len(w) == 5
        and set(w).issuperset(set(index[9]).difference(index[1]))
    )

    # 2 is the last one
    index[2] = next(w for w in inp if w not in index)

    return index


def part2():
    lines = read_input()
    total_sum = 0

    for inp, outp in lines:
        index = reveal(inp)
        real_out = "".join(
            next(str(i) for i, val in enumerate(index) if set(val) == set(num))
            for num in outp
        )
        total_sum += int(real_out)

    return total_sum


if __name__ == '__main__':
    print("Part 1", part1())
    print("Part 2", part2())
