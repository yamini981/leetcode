class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # iterate from the end of the string until the first non space character
        # then keep going until space again

        end = len(s) - 1

        while s[end] == " ":
            end -= 1
        start = end
        while s[start] != " " and start != 0:
            start -= 1

        if s[start] == " ":
            start += 1

        return end - start + 1