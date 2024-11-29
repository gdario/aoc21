from collections import deque
from functools import reduce
import math
import re


def read_number(num: str) -> list[list[int, int]]:
    level = 0
    res = []
    pieces = re.split(r"(\d+)", num)
    for piece in pieces:
        if piece.isnumeric():
            value = int(piece)
            res.append([value, level])
        else:
            level += piece.count("[") - piece.count("]")
    return res


def explode(num: list) -> bool:
    num_len = len(num)
    for i in range(num_len):
        if num[i][1] == 5:
            if i > 0:
                num[i-1] = [num[i-1][0] + num[i][0], num[i-1][1]]
            if (i+2) < num_len:
                num[i+2] = [num[i+2][0] + num[i+1][0], num[i+2][1]]
            num[i:i+2] = [[0, 4]]
            return True
    return False


def split(num: list) -> bool:
    num_len = len(num)
    for i in range(num_len):
        if num[i][0] >= 10:
            value, level = num[i][0], num[i][1]
            left, right = math.floor(value / 2), math.ceil(value / 2)
            num[i:i+1] = [[left, level+1], [right, level+1]]
            return True
    return False


def add(num1: list, num2: list) -> list[tuple[int, int]]:
    num = [[x[0], x[1] + 1] for x in num1] + [[y[0], y[1] + 1] for y in num2]
    while explode(num) or split(num):
        continue
    return num


def flat2tree(num: list) -> list:
    d = deque(num)

    def grab(level):
        return (d.popleft()[0] if d[0][1] == level
                else [grab(level+1), grab(level+1)])
    return grab(level=0)


def magnitude(num: list) -> int:
    # breakpoint()
    while len(num) > 1:
        for i in range(len(num)):
            left, right = num[i], num[i+1]
            if left[1] == right[1]:
                num[i:i+2] = [[3*left[0] + 2*right[0], left[1]-1]]
                break
    return num[0][0]


if __name__ == "__main__":
    with open('../data/d18_input_p1.txt', 'r') as fh:
        nums = fh.readlines()

    nums = [read_number(n) for n in nums]
    res = reduce(add, nums)
    print(magnitude(res))
