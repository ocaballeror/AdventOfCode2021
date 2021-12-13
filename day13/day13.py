def read_input():
    with open("input") as f:
        reading_dots = True
        dots = set()
        folds = []
        for line in f:
            line = line.strip()
            if reading_dots:
                if not line:
                    reading_dots = False
                    continue

                x, y = map(int, line.strip().split(","))
                dots.add((x, y))
            else:
                coord = line.split()[2]
                along, num = coord.split("=")
                folds.append((along, int(num)))

    return dots, folds


def part1():
    dots, folds = read_input()
    along, line = folds[0]
    new_grid = set()
    for x, y in dots:
        if along == "y" and y > line:
            y = line - (y - line)
        elif along == "x" and x > line:
            x = line - (x - line)

        new_grid.add((x, y))

    return len(new_grid)


def part2():
    dots, folds = read_input()

    for along, line in folds:
        new_grid = set()
        for x, y in dots:
            if along == "y" and y > line:
                y = line - (y - line)
            elif along == "x" and x > line:
                x = line - (x - line)

            new_grid.add((x, y))
        dots = new_grid

    maxx = max(a[0] for a in dots)
    maxy = max(a[1] for a in dots)
    grid = "\n".join(
        "".join("#" if (x, y) in dots else "." for x in range(maxx + 1))
        for y in range(maxy + 1)
    )
    return "\n" + grid


if __name__ == "__main__":
    print("Part 1", part1())
    print("Part 2", part2())
