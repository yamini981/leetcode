class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # L R where L = 0, R = 0
        # track current characters in a set with the count
        # want characters to replicate the most frequent character
        # in the set - will first be s[L]
        # track best character
        # if s[R] == s[L] it's good hooray, shift to the right
        # if s[R] != s[L] either a) increment the count or
        # b) if you can't increment the count, shift left forward by 1
        # and set right equal to left again

        freq = {}
        l, r = 0, 0
        currLongest = 1
        mostFrequentCharacter = s[l]

        while r != len(s):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            if freq[s[r]] > freq[mostFrequentCharacter]:
                mostFrequentCharacter = s[r]
            
            numManipulations = r - l + 1 - freq[mostFrequentCharacter]
            if numManipulations <= k:
                currLongest = max(currLongest, r - l + 1)
            else:
                freq[s[l]] -= 1
                l += 1
            r += 1

        return currLongest

