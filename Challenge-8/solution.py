class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        maxsum = 1
        minsum = 1
        for i in nums:
            curpro = maxsum * i
            maxsum = max(curpro, minsum * i, i)
            minsum = min(curpro, minsum * i, i)
            res = max(res, maxsum)
        return res
