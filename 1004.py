class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        zeros = 0
        res = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                while zeros >= k:
                    if nums[left] == 0:
                        zeros -= 1
                    left += 1
                zeros += 1
            res = max(right - left + 1, res)

        return res



s = Solution()
s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)

test_cases = [
    [
        [1,1,1,0,0,0,1,1,1,1,0], 2, 6
    ],
    [
        [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10
    ],
    [
        [0,0,0,1], 4, 4
    ]
]

for t in test_cases:
    got = s.longestOnes(t[0], t[1])
    assert t[-1] == got, f"n={t[0]}, k={t[1]}, got={got}, wants={t[-1]}"

