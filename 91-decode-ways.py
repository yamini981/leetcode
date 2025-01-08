class Solution:
    def numDecodings(self, s: str) -> int:
        
        curr = 0
        first = 1
        second = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                curr = 0
                
            else:
                curr = first
            
            if (i + 1 < len(s) and ((s[i] == '1') or (s[i] == '2' and s[i+1] in '0123456'))):
                curr += second
            
            tmp = first
            first = curr
            second = tmp
        
        return curr
        
