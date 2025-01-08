class Solution:
    def isValid(self, s: str) -> bool:
        # closing bracket can only exist if open bracket showed up first
        # should be queue of closing brackets
        # how to handle: (())?

        stack = []
        hashmap = {']':'[', ')':'(', '}':'{'}

        for char in s:
            if char not in hashmap:
                stack.append(char)
                continue

            if not stack or stack[-1] != hashmap[char]:
                return False
            stack.pop()

        return len(stack) == 0

        
