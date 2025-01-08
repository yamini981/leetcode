class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        bestPal = s[0]
        bestLength = 1

        for i in range(len(s)):
            #odd length
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                strLen = right - left + 1
                if strLen > bestLength:
                    bestPal = s[left: right +1]
                    bestLength = strLen
                left -= 1
                right += 1
            
            #even length
            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                strLen = right - left + 1
                if strLen > bestLength:
                    bestPal = s[left: right +1]
                    bestLength = strLen
                left -= 1
                right += 1
        
        return bestPal



        
