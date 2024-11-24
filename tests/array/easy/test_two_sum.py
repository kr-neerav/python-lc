from pytest import mark
from code.array.easy.two_sum import two_sum


@mark.parametrize('nums, target, expected', [
    ([3, 3], 6, [0, 1]),        # test with duplicate elements
    ([1, 2, 3, 4, 5, 6, 12, 13, 14], 20, [5, 8]),   # single output
    ([1, 2, 3, 4, 5, 6], 7, [2, 3]),    # multile outputs, returns the first one
    ([1, 2, 3, 4], 8, [])   # no output
])
def test_expected_outcome(nums: list[int], target: int, expected: list[int]):
    assert two_sum(nums, target) == expected
