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


def find_shift(x, y, previous_shift=np.array([0, 0, 0])):
    """Compute the position of a scanner w.r.t. to a reference scanner
    in case their beacons overlap to a sufficient extent."""
    for rotation in generate_rotations():
        R = generate_matrix(rotation)
        rotated_y = (R @ y.T).T
        res = cartesian_differences(x, rotated_y)
        if res[0][1] > 11:
            new_shift = np.array(res[0][0]) + previous_shift
            return new_shift, new_shift + rotated_y


def search(data):
    explored = {0}
    all_cubes = set(range(len(data)))
    queue = deque([0])
    probes = [data[0]]
    while queue:
        d = data[queue.pop()]
        for i in (all_cubes - explored):
            res = find_shift(d, data[i])
            if res is not None:
                probes.append(res)
                explored.add(i)
                queue.appendleft(i)
    out = np.concat(probes, axis=0)
    return np.unique(out, axis=0)


if __name__ == '__main__':
    data = read_data('../data/d19_test.txt')
    # (0,1), (1,3), (1,4), (2,4)
