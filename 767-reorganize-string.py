class Solution:
    def reorganizeString(self, s: str) -> str:
        # two pointer..? if we swap 2 characters we likely have to move back though
        # could just convert to a dictionary with character counts
        # and then recreate the string!
        charMap = {}
        max_count, max_char = 0, ''

        for char in s:
            currCount = charMap.get(char, 0) + 1
            charMap[char] = currCount
            if currCount > max_count:
                max_count = currCount
                max_char = char
        
        ans = [''] * len(s)
        i = 0
        if max_count > math.ceil(len(s) / 2):
            return ""
        while charMap[max_char] != 0:
            ans[i] = max_char
            charMap[max_char] -= 1
            i += 2
        for char, count in charMap.items():
            while count != 0:
                if i >= len(s):
                    i = 1
                ans[i] = char
                i += 2
                count -= 1
        return ''.join(ans)

        
        

        
        
