import sys


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        memo = [[sys.maxsize] * n for i in range(2)]
        memo[0][0] = triangle[0][0]

        for i in range(1, n):
            for j, num in enumerate(triangle[i]):
                memo[i % 2][j] = min(memo[(i-1)%2][j], memo[(i-1)%2][max(j - 1, 0)]) + triangle[i][j]
        
        return min(memo[(n - 1) % 2])


s = Solution()

test_cases = [
    [
        [[2],[3,4],[6,5,7],[4,1,8,3]], 11
    ],
    [
        [[-10]], -10
    ],
    [
        [[-1],[2,3],[1,-1,-3]], -1
    ]
]

for t in test_cases:
    got = s.minimumTotal(t[0])
    assert t[-1] == got, f"input={t[0]}, got={got}, wants={t[-1]}"

