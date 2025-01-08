class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        numIslands = 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        for r in range(ROWS):
            for c in range (COLS):
                if (r, c) in visited or grid[r][c] == '0':
                    continue
                
                queue = collections.deque()
                numIslands += 1
                queue.append((r, c))
                while queue:
                    currValue = queue.popleft()
                    if currValue in visited:
                        continue
                    visited.add(currValue)
                    currR = currValue[0]
                    currC = currValue[1]
                    if grid[currR][currC] == '0':
                        continue
                    if (currR - 1) >= 0:
                        queue.append((currR - 1, currC))
                    if (currR + 1) < ROWS:
                        queue.append((currR + 1, currC))
                    if (currC + 1) < COLS:
                        queue.append((currR, currC + 1))
                    if (currC - 1) >= 0:
                        queue.append((currR, currC - 1))

        return numIslands

        