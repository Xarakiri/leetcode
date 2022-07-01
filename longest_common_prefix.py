class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = ""
        i = 0
        while True:
            ok = True
            for str in range(0, len(strs)-1):
                if i+1 > len(strs[str]) or i+1 > len(strs[str+1]):
                    return answer
                ok = ok and (strs[str][i] == strs[str+1][i])
            if ok and i < len(strs[0]):
                answer += strs[0][i]
                i+=1
            else:
                return answer

            