class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_ = n * (n+1)//2 # сумма арифметической прогрессии
        return sum_ - sum(nums)
