class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        for char in s1:
            s1Count[char] = s1Count.get(char, 0) + 1
        
        def checkEqualCount(s1c, s2c):
            for i in range(26):
                currChar = chr(ord('a') + i)
                if s1c.get(currChar, 0) != s2c.get(currChar, 0):
                    return False
            return True


        s2Count = {}
        l = 0
        r = 0
        while r < len(s2):
            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1
            while s2Count[s2[r]] > s1Count.get(s2[r], 0):
                s2Count[s2[l]] = s2Count.get(s2[l]) - 1
                l += 1
            
            r += 1
            if checkEqualCount(s1Count, s2Count):
                return True
        return False
