class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        # i barely understand this I won't lie
        n = len(strength)
        mod = 10**9 + 7
        res = 0

        leftIndex = [-1] * n
        rightIndex = [n] * n
        presumOfPresum = [-1] * (n + 1)

        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                rightIndex[stack.pop()] = i
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                leftIndex[stack.pop()] = i
            stack.append(i)
        
        presumOfPresum = list(accumulate(accumulate(strength, initial = 0), initial = 0))

        for i in range(n):
            left_bound = leftIndex[i]
            right_bound = rightIndex[i]

            left_count = i - left_bound
            right_count = right_bound - i

            neg_presum = (presumOfPresum[i + 1] - presumOfPresum[i - left_count + 1]) % mod
            pos_presum = (presumOfPresum[i + right_count + 1] - presumOfPresum[i + 1]) % mod

            res += strength[i] * (pos_presum * left_count - neg_presum * right_count)
            res %= mod

        return res

        return res % mod