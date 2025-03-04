class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        backwardsNumber = 0
        while x > backwardsNumber:
            backwardsNumber = backwardsNumber * 10 + x % 10
            x = x // 10

        return x == backwardsNumber or x == backwardsNumber // 10
