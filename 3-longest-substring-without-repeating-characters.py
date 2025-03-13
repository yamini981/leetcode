class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l, r = 0, 0
        charsSeen = set()
        longest = 1
        while r < len(s):
            currChar = s[r]
            if currChar not in charsSeen:
                charsSeen.add(currChar)
                r += 1
            else:
                charsSeen.remove(s[l])
                l += 1
            longest = max(len(charsSeen), longest)
        return longest

