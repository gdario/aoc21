import re
import itertools


def flatten(x: list, level=0) -> list:
    if isinstance(x, int):
        return [(x, level)]
    else:
        return flatten(x[0], level+1) + flatten(x[1], level+1)


assert flatten([[1, 2], 3]) == [(1, 2), (2, 2), (3, 1)]
assert flatten([[1, 2], [3, 4]]) == [(1, 2), (2, 2), (3, 2), (4, 2)]
assert flatten([1, [2, [3, [4, 5]]]]) == [(1, 1), (2, 2), (3, 3),
                                          (4, 4), (5, 4)]
