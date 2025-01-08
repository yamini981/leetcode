class Solution:
    def reverse(self, x: int) -> int:
        isNegative = x < 0
        if isNegative:
            strX = str(-1 * x) 
        else:
            strX = str(x)

        maxStr = "2147483647"
        
        reversedInt = strX[::-1]
        if len(reversedInt) == 10:
            for i in range(10):
                if int(reversedInt[i]) > int(maxStr[i]):
                    return 0
                if int(reversedInt[i]) < int(maxStr[i]):
                    break
        finalNum = int(reversedInt)
        

        if isNegative:
            return finalNum * -1
        else:
            return finalNum