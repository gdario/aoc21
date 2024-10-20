from ast import List
from ctypes import Union
from dataclasses import dataclass
from typing import Iterable


def first(x: Iterable) -> int:
    return next(iter(x))


class Snum(list):
    """A list of Num components."""


@dataclass
class Num:
    """A regular number within a Snum annotated with the nesting level."""
    n: int
    level: int

# TODO: understand this recursive definition
Tree = Union[int, List['Tree']]


def snum_add(left: Snum, right: Snum) -> Snum:
    snum = Snum(Num(x.n, x.level + 1) for x in left + right)
    return snum_reduce(snum)


def snum_reduce(snum: Snum) -> Snum:
    while explode(snum) or split(snum):
        continue
    return snum


def split(snum: Snum) -> bool:
    i = first(i for i, s in enumerate(snum) if s.n >= 10)
    if i is None:
        return False
    else:
        level = snum[i].level
        left, right = snum[i].n // 2, (snum[i].n + 1) // 2
        snum[i] = Num(left, level + 1)
        snum.insert(i + 1, Num(right, level + 1))
        return True


def explode(snum: Snum) -> bool:
    i = first(i for i, s in enumerate(snum) if s.level > 4)
    if i is None:
        return False
    else:
        if i - 1 >= 0:
            snum[i - 1].n += snum[i].n
        if i + 2 < len(snum):
            snum[i + 2].n += snum[i + 1].n
        snum[i:i+2] = [Num(0, snum[i].level - 1)]
        return True

# NOTE: [int(x) for x in snum_str if x.isdigit()] would not parse numbers
# greater than 10 correctly, i.e., it would return the individual digits.
# This function is also much more "defensive" as it allows plain numbers
# outside of the list (level = 0)
def snum_from_str(snum_str: str) -> Snum:
    """Convert a string representing a snailfilsh number into a Snum."""
    level = 0
    result = []
    # Note the use of capturing groups in re.split. If not present, the
    # numbers would not be part of the results.
    for piece in re.split(r'(\d+)', snum_str):
        if piece[0] in '0123456789':
            result.append(Num(int(piece), level))
        else:
            level += piece.count('[') - piece.count(']')
    return result


def tree_from_snum(snum: Snum) -> Tree:
    q = deque(snum)
    def grab(level):
        return (q.popleft().n if q[0].level == level
                else [grab(level + 1), grab(level + 1)])
    return grab(level=0)


def main():
    pass
