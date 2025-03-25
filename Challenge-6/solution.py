class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        prefix = 1
        for i in range(1, len(nums)):
            prefix = prefix * nums[i-1]
            res[i] = prefix
        suffix = 1
        for j in range(len(nums) - 2, -1, -1):
            suffix = suffix * nums[j+1]
            res[j] = res[j] * suffix 
        return res
