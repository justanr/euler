from collections import deque
from functools import reduce
from itertools import islice
from operator import mul


def product(nums):
    return reduce(mul, nums, 1)


def sliding(it, size):
    it = iter(it)
    window = deque(islice(it, size), maxlen=size)
    yield tuple(window)
    for item in it:
        window.append(item)
        yield tuple(window)


def gather_numbers():
    nums = []
    with open('block.txt', 'r') as fh:
        for line in fh.readlines():
            nums.extend(int(n) for n in line.strip())
    return nums


def solution():
    return max(map(product, sliding(gather_numbers(), size=13)))

if __name__ == '__main__':
    print(solution())
