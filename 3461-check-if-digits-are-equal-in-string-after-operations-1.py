class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # can manually do it, but I'm sure there's a trick
        # very strange problem - good reminder to start with brute force!
        oldAns = [None] * len(s)
        ans = [None] * (len(s) - 1)
        for i in range(len(s)):
            oldAns[i] = int(s[i])
        
        while len(ans) > 1:
            for i in range(0, len(ans)):
                ans[i] = oldAns[i] + oldAns[i + 1]
            oldAns = [None] * (len(ans) - 1)
            ans, oldAns = oldAns, ans
        return oldAns[0]%10 == oldAns[1]%10
                
            
            
            