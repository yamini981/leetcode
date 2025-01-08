class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bestLength = 0
        l, r = 0, 0
        # add to set? or actually could just add to an array 
        # since only about 50 potential characters
        # gonna do set for the concept
        currChars = set()

        while r < len(s):
            if s[r] in currChars:
                currChars.remove(s[l])
                l += 1
            else:
                currChars.add(s[r])
                bestLength = max(bestLength, len(currChars))
                r += 1

        return bestLength
    


