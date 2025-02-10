class Solution:
    def clearDigits(self, s: str) -> str:
        # might be better to reconstruct the string
        digitPointer = 0
        ret = ""
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for i in range(len(s)):
            if s[i] not in digits:
                ret += s[i]
            else:
                ret = ret[:-1]
        return ret
                
