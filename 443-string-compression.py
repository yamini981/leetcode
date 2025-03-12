class Solution:
    def compress(self, chars: List[str]) -> int:

        # iterate through all characters
        pointer = 0
        prevChar = None
        currCount = 1
        for i in range(len(chars)):
            currChar = chars[i]
            if currChar != prevChar:
                miniStack = [currChar]
                if currCount > 1:
                    while currCount > 0:
                        miniStack.append(currCount % 10)
                        currCount //= 10
                while miniStack:
                    top = miniStack.pop()
                    chars[pointer] = str(top)
                    pointer += 1

                # pointer += 1
                currCount = 1
                prevChar = currChar
            else:
                currCount += 1
        
        miniStack = []
        if currCount > 1:
            while currCount > 0:
                miniStack.append(currCount % 10)
                currCount //= 10
        while miniStack:
            top = miniStack.pop()
            chars[pointer] = str(top)
            pointer += 1
        return pointer

