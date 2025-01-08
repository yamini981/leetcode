class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DP = [[1] * n] * m
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                DP[i][j] = DP[i+1][j] + DP[i][j + 1]
        return DP[0][0]