class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # put all characters in 't' into hashmap with count
        # then brute force for s would be O(n^2 m)
        # This is because you would go through every substring
        # in s then check if t is in that...
        # could do some sort of DP? minimum window substring from
        # just the first character of s, then the second, etc.
        # i would ask hint at this point i'm watching the damn neetcodde vid

        if t == "":
            return ""
        
        countT, window = {}, {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        have, need = 0, len(countT)
        res = [-1, -1]
        resLen = math.inf

        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                # update our result    
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
                
        l, r = res
        return s[l:r + 1] if resLen != math.inf else ""