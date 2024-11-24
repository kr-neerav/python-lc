def update_lkp(lkp: dict[int, list[int]], i: int, v: int) -> None:
    """Update the lookup dictionary with new index and value."""
    if v in lkp:
        lkp[v].append(i)
    else:
        lkp[v] = [i]

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers in nums that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        List containing indices of two numbers that add up to target
    """
    lkp = {}  # value -> list of indices
    for i in range(len(nums)):
        search_key = target - nums[i]
        if search_key in lkp:
            return [lkp[search_key][0], i]
        update_lkp(lkp, i, nums[i])
    return []
