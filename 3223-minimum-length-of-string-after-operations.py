class Solution:
    def minimumLength(self, s: str) -> int:
        # is every removal good? Yes
        minLength = len(s)
        chars = {}
        for i in range(len(s)):
            chars[s[i]] = chars.get(s[i], 0) + 1
        # key = s[i], val = count of s[i]
        for key, val in chars.items():
            if val % 2 == 0:
                minLength -= (val - 2)
            elif val != 1:
                minLength -= (val - 1)

        return minLength

