import math


class Number:
    def __init__(self, x: list) -> None:
        self.x = x
        self.xflat = []
        self.flatten(x)

    def flatten(self, x: list, level: int = 0) -> tuple:
        for item in x:
            if isinstance(item, list):
                self.flatten(item, level+1)
            else:
                self.xflat.append((item, level))

    def is_not_split(self):
        res = any([x[0] >= 10 for x in self.xflat])
        return res

    def is_not_exploded(self):
        res = any([x[1] == 4 for x in self.xflat])
        return res

    def explode(self):
        for k, item in enumerate(self.xflat):
            if item[1] >= 4:
                if k > 0:
                    left = self.xflat[k-1]
                    self.xflat[k-1] = (item[0] + left[0], left[1])
                if k < len(self.xflat) - 2:
                    right = self.xflat[k+2]
                    self.xflat[k+2] = (
                        self.xflat[k+1][0] + right[0], right[1])
                self.xflat.pop(k)
                self.xflat.pop(k)
                self.xflat.insert(k, (0, 3))
                break

    def split(self):
        for k, item in enumerate(self.xflat):
            if item[0] >= 10:
                left, right = math.floor(item[0] / 2), math.ceil(item[0] / 2)
                self.xflat[k] = (left, item[1] + 1)
                self.xflat.insert(k + 1, (right, item[1] + 1))
                break

    def reduce(self):
        while self.is_not_split or self.is_not_exploded:
            if self.is_not_split():
                self.split()
            else:
                self.explode()

    def __add__(self, other):
        x = [self.x, other.x]
        res = Number(x)
        # res.reduce()
        return res
