class Solution:
    def reverseBits(self, n: int) -> int:
        retVal = 0
        for i in range(0, 32):
            retVal = retVal << 1
            retVal += (n >> i) & 1
            

        return retVal