class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                return True
            dic[n] = i
        return False
