from functools import reduce
import src.day18 as d18


def test_read_number():
    assert d18.read_number("[1, [2, 3]]") == [[1, 1], [2, 2], [3, 2]]
    assert d18.read_number("[[1, 2], [[3, 4], 5], 6]") == [
        [1, 2], [2, 2], [3, 3], [4, 3], [5, 2], [6, 1]]
    assert d18.read_number("[[[[[9,8],1],2],3],4]") == [
        [9, 5], [8, 5], [1, 4], [2, 3], [3, 2], [4, 1]]
    assert d18.read_number("[[[[0,9],2],3],4]") == [
        [0, 4], [9, 4], [2, 3], [3, 2], [4, 1]]


def test_explode():
    num = [[9, 5], [8, 5], [1, 4], [2, 3], [3, 2], [4, 1]]
    _ = d18.explode(num)
    assert num == [[0, 4], [9, 4], [2, 3], [3, 2], [4, 1]]
    num = [[6, 2], [5, 3], [4, 4], [3, 5], [2, 5], [1, 1]]
    _ = d18.explode(num)
    assert num == [[6, 2], [5, 3], [7, 4], [0, 4], [3, 1]]
    num = [[1, 1], [2, 2], [3, 2]]
    assert not d18.explode(num)


def test_split():
    num = [[1, 1], [11, 2], [2, 2]]
    _ = d18.split(num)
    assert num == [[1, 1], [5, 3], [6, 3], [2, 2]]
    num = [[1, 1], [2, 2], [3, 2]]
    assert not d18.split(num)


def test_sum():
    num1 = [[4, 4], [3, 4], [4, 3], [4, 2], [7, 2], [8, 4], [4, 4], [9, 3]]
    num2 = [[1, 1], [1, 1]]
    actual = d18.add(num1, num2)
    expected = d18.read_number("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
    assert actual == expected


def test_flat2tree():
    assert d18.flat2tree([[1, 1], [1, 1]]) == [1, 1]
    assert d18.flat2tree([[1, 1], [2, 2], [3, 2]]) == [1, [2, 3]]


def test_magnitude():
    num = [[9, 1], [1, 1]]
    assert d18.magnitude(num) == 29
    num = [[9, 2], [1, 2], [1, 2], [9, 2]]
    assert d18.magnitude(num) == 129
    num = d18.read_number('[[[[5,0],[7,4]],[5,5]],[6,6]]')
    assert d18.magnitude(num) == 1137


def test_long_sum():
    nums = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".splitlines()
    nums = [d18.read_number(n) for n in nums]
    res = reduce(d18.add, nums)
    expected = d18.read_number(
        '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]')
    assert res == expected
    assert d18.magnitude(res) == 4140
