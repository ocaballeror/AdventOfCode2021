import itertools
from multiprocessing import Pool


class MutInt:
    """Mutable int for easier replacements"""

    def __init__(self, val: int):
        if isinstance(val, MutInt):
            self.val = val.val
        else:
            self.val = int(val)

    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.val == other.val
        return self.val == other

    def __ge__(self, other):
        if isinstance(other, MutInt):
            return self.val >= other.val
        return self.val >= other

    def __add__(self, other):
        if isinstance(other, MutInt):
            return self.val + other.val
        return self.val + other

    def __mul__(self, other):
        if isinstance(other, MutInt):
            return self.val * other.val
        return self.val * other

    def __floordiv__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.val // other.val)
        return MutInt(self.val // other)

    def __truediv__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.val / other.val)
        return self.val / other

    def __repr__(self):
        return str(self.val)


def to_mutint(line):
    return [MutInt(x) if isinstance(x, int) else to_mutint(x) for x in line]


def read_input():
    with open("input") as f:
        return [to_mutint(eval(line)) for line in f]


def _explode(nums, depth=0):
    first, second = nums
    left, right = MutInt(0), MutInt(0)

    if isinstance(first, MutInt) and isinstance(second, MutInt) and depth >= 4:
        return first, MutInt(0), second

    if isinstance(first, list):
        left, first, midleft = _explode(first, depth + 1)

        if second:
            other = second
            while isinstance(other, list):
                other = other[0]
            other.val += midleft.val

    if isinstance(second, list):
        midright, second, right = _explode(second, depth + 1)

        if first:
            other = first
            while isinstance(other, list):
                other = other[-1]
            other.val += midright.val

    return left, [first, second], right


def explode(numbers):
    a, numbers, b = _explode(numbers)
    return numbers


def _split(numbers):
    first, second = numbers
    done = False
    if isinstance(first, MutInt) and first >= 10:
        first = [MutInt(first // 2), MutInt(first / 2 + 0.5)]
        done = True
    elif isinstance(first, list):
        done, first = _split(first)

    if not done:
        if isinstance(second, MutInt) and second >= 10:
            second = [MutInt(second // 2), MutInt(second / 2 + 0.5)]
            done = True
        elif isinstance(second, list):
            done, second = _split(second)

    return done, [first, second]


def split(numbers):
    return _split(numbers)[1]


def reduce(numbers):
    while True:
        new = explode(numbers)
        new = split(new)

        if new == numbers:
            break

        numbers = new

    return numbers


def lsum(lst):
    numbers = lst[0]
    for line in lst[1:]:
        numbers = reduce([numbers, line])

    return numbers


def magnitude(numbers):
    first, second = numbers
    if isinstance(first, list):
        first = magnitude(first)

    if isinstance(second, list):
        second = magnitude(second)

    return first * 3 + second * 2


def part1():
    return magnitude(lsum(read_input()))


def rank(pairs):
    return magnitude(lsum(pairs))


def part2():
    data = read_input()
    pairs = itertools.permutations(data, 2)
    with Pool() as pool:
        best = 0
        for res in pool.imap_unordered(rank, pairs):
            if res > best:
                best = res

    return best


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
