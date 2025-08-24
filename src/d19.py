from collections import Counter, deque
import itertools as it
import numpy as np


def read_data(file):
    beacons = []
    current_beacon = []
    with open(file, 'r') as fh:
        for line in fh:
            if line.startswith('--- '):
                continue
            elif line == '\n':
                beacons.append(np.array(current_beacon))
                current_beacon = []
            else:
                current_beacon.append([
                    int(x) for x in line.strip().split(',')])
    return beacons


def generate_rotations():
    """Generate a tuple containing the first two axes of the rotation matrix
    and their orientations."""
    signs = it.product((-1, 1), (-1, 1))
    axes = it.permutations(((1, 0, 0), (0, 1, 0), (0, 0, 1)), 2)
    rotations = it.product(signs, axes)
    return rotations


def generate_matrix(x):
    """Generate the rotation matrix corresponding to rotation x.
    All the matrices have unit determinants."""
    signs, axes = x
    signed_arrays = [x[0][i] * np.array(x[1][i]) for i in (0, 1)]
    signed_arrays.append(np.cross(signed_arrays[0], signed_arrays[1]))
    return np.array(signed_arrays).T


def cartesian_differences(x, y):
    """Return the most common shift vector between two sets of points represen-
    test as matrices x and y. x is the reference scanner."""
    prods = it.product(x, y)
    diffs = it.starmap(np.subtract, prods)
    return Counter(tuple(d.tolist()) for d in diffs).most_common(1)


def find_shift(x, y, overlap_thr=12):
    """Compute the position of a scanner w.r.t. to a reference scanner
    in case their beacons overlap to a sufficient extent."""
    for rotation in generate_rotations():
        rotation_matrix = generate_matrix(rotation)
        rotated_y = (rotation_matrix @ y.T).T
        res = cartesian_differences(x, rotated_y)
        if res[0][1] >= overlap_thr:
            shift = np.array(res[0][0])
            return shift, shift + rotated_y

def search(data):
    matrices = [data[0]]
    queue = deque([data[0]])
    explored = {0}
    scanners = [np.array([0, 0, 0])]
    while queue:
        d = queue.pop()
        for i in range(len(data)):
            if i not in explored:
                res = find_shift(d, data[i])
                if res is not None:
                    explored.add(i)
                    queue.append(res[1])
                    matrices.append(res[1])
                    scanners.append(res[0])
    return np.unique(np.concat(matrices, axis=0), axis=0), scanners


def manhattan_distance(b1, b2):
    """Manhattan distance between two beacons."""
    return abs(b1 - b2).sum()


def part1():
    # data = read_data("../data/d19_test.txt")
    data = read_data("../data/d19_input_p1.txt")
    res, scanners = search(data)
    print(f"Number of beacons: {res.shape}")
    max_dist = 0
    for i in range(len(scanners) - 1):
        for j in range(i, len(scanners)):
            d = manhattan_distance(scanners[i], scanners[j])
            if d > max_dist:
                max_dist = d
    print(f"Max. Manhattan distance among scanners: {max_dist}")


if __name__ == '__main__':
    part1()
    # (0,1), (1,3), (1,4), (2,4)
    # d1 = find_shift(data[0], data[1])
    # d4 = find_shift(d1, data[4])
    # d3 = find_shift(d1, data[3])
    # d2 = find_shift(d4, data[2])
    # res = [data[0], d1, d2, d3, d4]
    # out = np.unique(np.concat(res, axis=0), axis=0)
    # print(out.shape[0])  # 79
    # data = read_data("../data/d19_input_p1.txt")
    
