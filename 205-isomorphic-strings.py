class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # characters in 's' map to a character in 't'
        sMap = {}
        tSet = set()

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            currChar = s[i] 
            if currChar not in sMap:
                sMap[currChar] = t[i]
                if t[i] in tSet:
                    return False
                tSet.add(t[i])
                
            else:
                if sMap[currChar] != t[i]:
                    return False

        return True