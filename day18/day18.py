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
