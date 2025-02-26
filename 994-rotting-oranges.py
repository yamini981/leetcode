class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # not optimal - should have done BFS instead!
        
        directions = [1, 0], [0, 1], [-1, 0], [0, -1]
        m = len(grid)
        n = len(grid[0])
        print(m, n)

        def dfsFreshToRotten(i, j, distTravelled, visited):
            if grid[i][j] == 0:
                return float('inf')
            if grid[i][j] == 2:
                return distTravelled
            retVal = float('inf')
            for dr, dc in directions:
                if (i + dr < m and i + dr >= 0 and j + dc < n and j + dc >= 0
                and (i + dr, j + dc) not in visited):
                    print(i + dr, j + dc)
                    visited.add((i + dr, j + dc))
                    visitedCopy = set(visited)
                    retVal = min(retVal, dfsFreshToRotten(i + dr, j + dc, distTravelled + 1, visitedCopy))
            return retVal
                    

        longestShortPath = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited = set([(i, j)])
                    dfsRet = dfsFreshToRotten(i, j, 0, visited)
                    print(i, j, dfsRet)
                    if dfsRet == float('inf'):
                        return -1
                    else:
                        longestShortPath = max(dfsRet, longestShortPath)

        return longestShortPath

                