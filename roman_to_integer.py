class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        answer = 0
        i = 0
        while i < len(s):
            not_at_end = i != (len(s) - 1)
            if not_at_end:
                if s[i] == "I":
                    if s[i+1] == "V":
                        answer += 4
                        i += 2
                        continue
                    elif s[i+1] == "X":
                        answer += 9
                        i += 2
                        continue
                if s[i] == "X":
                    if s[i+1] == "L":
                        answer += 40
                        i+=2
                        continue
                    if s[i+1] == "C":
                        answer += 90
                        i+=2
                        continue
                if s[i] == "C":
                    if s[i+1] == "D":
                        answer += 400
                        i+=2
                        continue
                    if s[i+1] == "M":
                        answer += 900
                        i+=2
                        continue
            answer += d[s[i]]
            i +=1
        return answer
