class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s
        retStr = s[0] + s[1]
        charCount = 2
        for i in range(2, len(s)):
            prev2 = retStr[charCount - 2]
            prev1 = retStr[charCount - 1]

            if prev1 == prev2 == s[i]:
                continue
            retStr += s[i]
            charCount += 1
        
        return retStr
            