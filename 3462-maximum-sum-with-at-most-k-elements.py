class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # we are given k elements to take from our grid
        # each row must not exceed the limit
        # we must take the biggest 'limits[i]' values from each row
        # could sort each list in grid -> O(nlogn * m)

        for lizt in grid:
            lizt.sort()
        
        bestNumbers = []
        for i in range(len(grid)):
            lizt = grid[i]
            for i in range(len(lizt) - 1, len(lizt) - limits[i] - 1, -1):
                bestNumbers.append(lizt[i])
        
        bestNumbers.sort()
        total = 0
        for i in range(len(bestNumbers) - 1, len(bestNumbers) - k - 1, -1):
            total += bestNumbers[i]
        
        return total
