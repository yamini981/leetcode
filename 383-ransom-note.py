class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap = {}

        for char in magazine:
            magazineMap[char] = 1 + magazineMap.get(char, 0)
        
        for char in ransomNote:
            magazineMap[char] = magazineMap.get(char, 0) - 1
            if magazineMap[char] == -1:
                return False

        return True