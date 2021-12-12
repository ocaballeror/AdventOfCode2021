OPENER = "[{(<"


class CorruptLine(Exception):
    pass


class IncompleteLine(Exception):
    pass


def read_input():
    with open("input") as f:
        return f.read().splitlines()


def closer(char):
    return {
        "[": "]",
        "{": "}",
        "(": ")",
        "<": ">",
    }[char]


def balanced(line):
    while line:
        move = _balanced(line)
        if move == 0:
            return line[0]
        line = line[move:]


def _balanced(line):
    total_move = 0
    head = line[0]
    rest = line[1:]

    if not rest:
        raise IncompleteLine(closer(head))

    if closer(head) == rest[0]:
        return 2

    while rest and rest[0] in OPENER:
        move = _balanced(rest)
        if move < 1:
            return move

        rest = rest[move:]
        total_move += move

    if not rest:
        raise IncompleteLine(closer(head))

    if closer(head) == rest[0]:
        return total_move + 2

    raise CorruptLine(rest[0])


def part1():
    lines = read_input()
    score = 0
    for line in lines:
        try:
            balanced(line)
        except CorruptLine as ex:
            score += {')': 3, ']': 57, '}': 1197, '>': 25137}[ex.args[0]]
            continue
        except IncompleteLine:
            pass

    return score


def part2():
    lines = read_input()
    scores = []
    for line in lines:
        score = 0
        while True:
            try:
                balanced(line)
            except CorruptLine:
                break
            except IncompleteLine as ex:
                points = {')': 1, ']': 2, '}': 3, '>': 4}[ex.args[0]]
                score = score * 5 + points
                line += ex.args[0]
            else:
                scores.append(score)
                break

    return sorted(scores)[len(scores) // 2]


if __name__ == '__main__':
    print("Part 1", part1())
    print("Part 2", part2())
