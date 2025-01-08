class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        ret = []

        mapping = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'), '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'), '9': ('w','x','y','z')}

        def dfs(currString, currIndex):
            if currIndex == len(digits):
                ret.append(currString)
                return
            currDigit = digits[currIndex]
            for char in mapping[currDigit]:
                dfs(currString + char, currIndex + 1)
            
        dfs("", 0)
        return ret
