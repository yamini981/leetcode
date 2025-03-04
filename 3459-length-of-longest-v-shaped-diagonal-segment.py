class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:

        # TLE'd - could use DP potentially but bruh
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        m = len(grid)
        n = len(grid[0])

        def currDirToClockwise(dr, dc):
            if dr == 1 and dc == 1:
                return (1, -1)
            if dr == -1 and dc == 1:
                return (1, 1)
            if dr == -1 and dc == -1:
                return (-1, 1)
            if dr == 1 and dc == -1:
                return (-1, -1)
        visited = set()
        def dfs(i, j, visited, shouldBe2, hasTurned, currLen, prevDirection, firstRun):
            bestLen = currLen
            visited.add((i, j))
            for dr, dc in directions:
                # check if in bounds first
                if (0 <= i + dr < m and 0 <= j + dc < n):
                    # check if it's been visited already
                    if ((i + dr, j + dc) not in visited):
                        # check correct value
                        if ((shouldBe2 and grid[i + dr][j + dc] == 2) or
                        not shouldBe2 and grid[i + dr][j + dc] == 0):
                            # check directions
                            # on firstRun, can go any direction
                            if (firstRun):
                                bestLen = max(bestLen, 
                                dfs(i + dr, j + dc, visited, not shouldBe2, hasTurned, currLen + 1, (dr, dc), False))
                                visited.remove((i + dr, j + dc))
                            # if has turned, can only go in the same direction
                            elif (hasTurned and dr == prevDirection[0] and 
                                dc == prevDirection[1]):
                                bestLen = max(bestLen, 
                                dfs(i + dr, j + dc, visited, not shouldBe2, hasTurned, currLen + 1, prevDirection, False))
                                visited.remove((i + dr, j + dc))
                            # if hasn't turned, can NOT go in prevDirection * -1
                            elif (not hasTurned and (dr != prevDirection[0] * -1 or dc != prevDirection[1] * -1)):
                                # if same direction
                                if dr == prevDirection[0] and dc == prevDirection[1]:
                                    bestLen = max(bestLen, 
                                    dfs(i + dr, j + dc, visited, not shouldBe2, False, currLen + 1, prevDirection, False))
                                    visited.remove((i + dr, j + dc))
                                # if changing directions MUST be going clockwise
                                else:
                                    clockwiseDir = currDirToClockwise(prevDirection[0], prevDirection[1])
                                    if dr == clockwiseDir[0] and dc == clockwiseDir[1]:
                                        bestLen = max(bestLen, 
                                        dfs(i + dr, j + dc, visited, not shouldBe2, True, currLen + 1, (dr, dc), False))
                                        visited.remove((i + dr, j + dc))
            return bestLen



        bestV = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited = set()
                    bestV = max(bestV, dfs(i, j, visited, True, False, 1, (0, 0), True))

        return bestV