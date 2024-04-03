def solution(numbers: [int]):
    """
    Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.

    Given an array of integers numbers,
    your task is to check all the triples of its consecutive elements for being a zigzag.
    More formally, your task is to construct an array of length numbers.length - 2, where the ith element
    of the output array equals 1 if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.

    3 ≤ numbers.length ≤ 100,
    1 ≤ numbers[i] ≤ 109.
    :param numbers:
    :return:
    """
    n = len(numbers)
    res = []
    for i in range(n - 2):
        result = is_zigzag(numbers[i], numbers[i + 1], numbers[i + 2])
        res.append(1 if result else 0)
    return res


def is_zigzag(a, b, c):
    return (a < b and b > c) or (a > b and b < c)
