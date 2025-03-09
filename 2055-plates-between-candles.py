class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # prefix sum
        n = len(s)
        prefixSum = [0] * n
        pointerOfLeftPlate = [0] * n
        pointerOfRightPlate = [0] * n

        # leading or ending plates will never be used
        # * * * | * * | * * * * * | * * | | *  *  |  *
        # 0 0 0 0 1 2 2 3 4 5 6 7 7 8 9 9 9 10 11 11 12
        
        firstPlateFound = False
        for i in range(n):
            char = s[i]
            if char == '*':
                if firstPlateFound:
                    prefixSum[i] = prefixSum[i - 1] + 1
                    pointerOfLeftPlate[i] = pointerOfLeftPlate[i - 1]
                else:
                    prefixSum[i] = 0
                    pointerOfLeftPlate[i] = 0
            elif char == "|":
                firstPlateFound = True
                if i > 0:
                    prefixSum[i] = prefixSum[i - 1]
                else:
                    prefixSum[i] = 0
                
                pointerOfLeftPlate[i] = i

        firstPlateFound = False
        for j in range(n - 1, -1, -1):
            char = s[j]
            if char == '*':
                if firstPlateFound:
                    pointerOfRightPlate[j] = pointerOfRightPlate[j + 1]
                else:
                    pointerOfRightPlate[j] = n - 1
            elif char == '|':
                firstPlateFound = True
                pointerOfRightPlate[j] = j
                
        ans = [0] * len(queries)

        for i in range(len(queries)):
            first = queries[i][0]
            second = queries[i][1]
            r = pointerOfLeftPlate[second]
            l = pointerOfRightPlate[first]
            if l >= r:
                ans[i] = 0
            else:
                ans[i] = prefixSum[r] - prefixSum[l]
        
        return ans