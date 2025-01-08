class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # sliding window starting at 0, k
        n = len(code)
        ret = [0] * len(code)
        if k == 0:
            return ret
        if k > 0:
            l = 0
            r = k
            currSum = sum(code[l:r + 1])
            for i in range(0, n):
                ret[i] = currSum - code[i]

                r += 1
                if (r == n):
                    r = 0
                currSum = currSum - code[l] + code[r]
                l += 1
        else: # k < 0:
            r = n - 1
            l = r + k
            currSum = sum(code[l:r+1])
            for j in range(n - 1, -1, -1):
                ret[j] = currSum - code[j]

                l -= 1
                if (l == -1):
                    l = n - 1

                currSum = currSum + code[l] - code[r]
                r -= 1

        return ret
                

                

