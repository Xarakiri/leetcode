class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = 0
        for i in nums:
            mask ^= i
        return mask
