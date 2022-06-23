import re


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reversed = 0
        tmp = x
        while tmp > 0:
            reversed = reversed*10 + tmp%10
            tmp = tmp//10
        return reversed == x
