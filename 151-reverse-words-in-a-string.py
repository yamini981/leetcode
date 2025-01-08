class Solution:
    def reverseWords(self, s: str) -> str:
        # can do s.split(' ') but the issue is the spaces
        # ok we can just split and then ignore ' '
        # O(n) time but O(n) space
        words = s.split(' ')
        words.reverse()

        newString = ""

        for word in words:
            if word == '':
                continue
            newString += word + ' '
        
        return newString[:len(newString) - 1]