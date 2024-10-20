import math


class Number:
    def __init__(self, x: list) -> None:
        # self.x = x
        self.flat = []
        self.flatten(x)

    def flatten(self, x: list, level: int = 0) -> tuple:
        for item in x:
            if isinstance(item, list):
                self.flatten(item, level + 1)
            else:
                self.flat.append((item, level))

    def reduce(self):
        for k, item in enumerate(self.flat):
            if item[1] == 4:
                self.explode(k)
                return True
            elif item[0] >= 10:
                self.split(k)
                return True
        return False

    def explode(self, k: int):
        item = self.flat[k]
        if k > 0:
            left = self.flat[k - 1]
            self.flat[k - 1] = (item[0] + left[0], left[1])
        if k < len(self.flat) - 2:
            right = self.flat[k + 2]
            self.flat[k + 2] = (self.flat[k + 1][0] + right[0], right[1])
        self.flat.pop(k)
        self.flat.pop(k)
        self.flat.insert(k, (0, 3))

    def split(self, k):
        item = self.flat[k]
        left, right = math.floor(item[0] / 2), math.ceil(item[0] / 2)
        self.flat[k] = (left, item[1] + 1)
        self.flat.insert(k + 1, (right, item[1] + 1))

    def __add__(self, other):
        res = Number([])
        flat1 = [(x[0], x[1]+1) for x in self.flat] 
        flat2 = [(x[0], x[1]+1) for x in other.flat] 
        res.flat = flat1 + flat2
        to_reduce = True
        while to_reduce:
            to_reduce = res.reduce()
        return res


if __name__ == "__main__":
    num = Number([[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]])
    num.reduce()
    res = Number([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]])
    assert num.flat == res.flat

    numbers = [
        [[[[[9, 8], 1], 2], 3], 4],
        [7, [6, [5, [4, [3, 2]]]]],
        [[6, [5, [4, [3, 2]]]], 1],
        [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]],
        [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
    ]
    results = [
        [[[[0, 9], 2], 3], 4],
        [7, [6, [5, [7, 0]]]],
        [[6, [5, [7, 0]]], 3],
        [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
        [[3, [2, [8, 0]]], [9, [5, [7, 0]]]],
    ]

    for k, number in enumerate(numbers):
        num = Number(number)
        num.reduce()
        res = Number(results[k])
        assert num.flat == res.flat

    # Test an addition
    # num1 = Number([[[[4, 3], 4], 4], [7, [[8, 4], 9]]])
    # num2 = Number([1, 1])
    # num3 = num1 + num2
    # res = Number([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]])
    # assert num3.flat == res.flat

    num1 = Number([[[[3, 0], [5, 3]], [4, 4]], [5, 5]])
    num2 = Number([6, 6])
    res = num1 + num2
    print(res.flat)

    x1 = [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
    x2 = [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
    num1 = Number(x1)
    num2 = Number(x2)
    num3 = Number([x1, x2])
    res = num1 + num2
    print(res.flat)
    print(num3.flat)