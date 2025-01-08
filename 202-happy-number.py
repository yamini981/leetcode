class Solution:
    def isHappy(self, n: int) -> bool:
        numSet = set()

        currValue = n
        while currValue not in numSet:
            numSet.add(currValue)
            newNum = 0

            while currValue != 0:
                newNum += (currValue % 10) * (currValue % 10)
                currValue = currValue // 10
            if newNum == 1:
                return True

            currValue = newNum
        return False