class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {
            "(": ")",
            "[": "]",
            "{": "}",
            ")": "",
            "}": "",
            "]": "",
        }

        stack = [s[0]]

        for p in s[1:]:
            if len(stack) == 0:
                stack.append(p)
                continue
            if (p == ")" or p == "}" or p == "]") and p == match[stack[-1]]:
                stack.pop()
            else:
                stack.append(p)
        return len(stack) == 0
