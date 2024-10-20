def partial_magnitude(x: list) -> bool:
    if len(x) == 1:
        return False
    for i in range(len(x)):
        if x[i][1] == x[i+1][1]:
            left, right, level = (x[i][0], x[i+1][0], x[i][1])
            x[i:i+2] = [(3*left + 2*right, level-1)]
            return True


def magnitude(x: list) -> int:
    y = x.copy()
    while(partial_magnitude(y)):
        pass
    return y[0][0]


if __name__ == '__main__':
    x = [(1, 1), (2, 1)]
    assert magnitude(x) == 7
    x = [(1, 2), (2, 2), (3, 1)]
    assert magnitude(x) == 27
    x = [(1, 2), (2, 2), (3, 3), (4, 3), (5, 2)]
    assert magnitude(x) == 143
    x = [(0, 4), (7, 4), (4, 3), (7, 4), (8, 4), (6, 4), (0, 4),
         (8, 2), (1, 2)]
    assert magnitude(x) == 1384
    
