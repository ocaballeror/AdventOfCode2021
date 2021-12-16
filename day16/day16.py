import functools
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Packet:
    version: int
    typeid: int
    value: Optional[int] = None
    subpackets: List["Packet"] = field(default_factory=list)

    def calculate(self):
        subs = [sub.calculate() for sub in self.subpackets]

        if self.typeid == 0:
            return sum(subs)
        if self.typeid == 1:
            return functools.reduce(lambda acc, sub: acc * sub, subs, 1)
        if self.typeid == 2:
            return min(subs)
        if self.typeid == 3:
            return max(subs)
        if self.typeid == 4:
            return self.value
        if self.typeid == 5:
            return subs[0] > subs[1]
        if self.typeid == 6:
            return subs[0] < subs[1]
        if self.typeid == 7:
            return subs[0] == subs[1]


def take(it, n) -> int:
    """ Consume n items from the generator it and convert the result to int """
    return int("".join(next(it) for _ in range(n)), base=2)


def parse(datait) -> Packet:
    version = take(datait, 3)
    typeid = take(datait, 3)

    if typeid == 4:
        num = 0
        while True:
            pre = take(datait, 1)
            num = (num << 4) + take(datait, 4)
            if pre == 0:
                break
        return Packet(version=version, typeid=typeid, value=num)

    sub = []
    lentype = take(datait, 1)
    if lentype == 0:
        length = take(datait, 15)
        rest = (next(datait) for _ in range(length))
        while True:
            try:
                sub.append(parse(rest))
            except RuntimeError:
                # generator will raise RuntimeError instead of StopIteration when finished
                break
    else:
        npackets = take(datait, 11)
        sub.extend(parse(datait) for _ in range(npackets))

    return Packet(version=version, typeid=typeid, subpackets=sub)


def versum(packet: Packet):
    return packet.version + sum(versum(sub) for sub in packet.subpackets)


def read_input():
    with open("input") as f:
        hexa = f.read().strip()
        bina = bin(int(hexa, base=16))[2:]  # remove '0b' prefix
        bina = bina.zfill(len(hexa) * 4)  # optionally pad beginning with zeros to match expected length
        return bina


def part1():
    return versum(parse(iter(read_input())))


def part2():
    packet = parse(iter(read_input()))
    return packet.calculate()


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
