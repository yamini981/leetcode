class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # thinking hashmap
        if len(s) != len(t):
            return False
        sMap, tMap = {}, {}

        for char in s:
            sMap[char] = 1 + sMap.get(char, 0)
        for char in t:
            tMap[char] = 1 + tMap.get(char, 0)
        
        for key in sMap:
            if sMap[key] != tMap.get(key, -1):
                return False
        return True