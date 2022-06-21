class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Naive solution
        # return len(set(nums)) != len(nums)

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
