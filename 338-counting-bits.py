class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ans = [0] * (n + 1)
        ans[1] = 1
        offset = 1
        for i in range(2, n + 1):
            if (i & (i - 1) == 0):
                offset *= 2
                ans[i] = 1
                continue
            ans[i] = 1 + ans[i - offset]

        return ans

