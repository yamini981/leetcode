class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longestLen = 1
        currLen = 0
        currChars = set()
        l, r = 0, 0
        while r < len(s):
            c = s[r]
            while c in currChars:
                currChars.remove(s[l])
                l += 1
                currLen -= 1
            # c will def not be in currChars now
            currLen += 1
            currChars.add(c)
            r += 1
            longestLen = max(currLen, longestLen)

        return longestLen

