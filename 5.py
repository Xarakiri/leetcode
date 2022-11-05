class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''

        def get_pal(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            op1, op2 = get_pal(s, i, i), get_pal(s, i, i + 1)
            if len(op1) > len(res):
                res = op1
            if len(op2) > len(res):
                res = op2

        return res


s = Solution()

test_cases = [
    [
        "babad", "bab"
    ],
    [
        "cbbd", "bb"
    ],
]

for t in test_cases:
    got = s.longestPalindrome(t[0])
    assert t[-1] == got, f"input={t[0]}, got={got}, wants={t[-1]}"

