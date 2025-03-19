def two_sum(nums, target):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    num_dict = {}
    n = len(nums)
    for i in range(n):
        dif = target - nums[i]
        if dif in num_dict:
            return [num_dict[dif], i]
        num_dict[nums[i]] = i