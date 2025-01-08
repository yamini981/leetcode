class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sIndex, tIndex = 0, 0
        if len(s) == 0:
            return True

        while tIndex < len(t):
            if s[sIndex] == t[tIndex]:
                sIndex += 1
            tIndex += 1
            if sIndex == len(s):
                return True
        return False