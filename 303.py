class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        sums = []
        current_sum = 0
        for num in nums:
            current_sum += num
            sums.append(current_sum)
        self.sums = sums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)