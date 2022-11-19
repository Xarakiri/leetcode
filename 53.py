class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            current_sum = max(current_sum + num, num)
            max_sum = max(current_sum, max_sum)

        return max_sum
