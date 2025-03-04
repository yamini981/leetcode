class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # visited = set()

        q = deque()
        numFreshOranges = 0
        # iterate through grid and add rotten oragnes to queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    numFreshOranges += 1
        
        minutesElapsed = 0
        if numFreshOranges == 0:
            return 0
        while q:
            print(q)
            for _ in range(len(q)):
                currVal = q.popleft()
                i, j = currVal
                for dx, dy in directions:
                    if (i + dx < m and i + dx >= 0 and
                    j + dy < n and j + dy >= 0 and
                    grid[i + dx][j + dy] == 1):
                        grid[i + dx][j + dy] = 2
                        numFreshOranges -= 1
                        q.append((i + dx, j + dy))
            minutesElapsed += 1
            if numFreshOranges == 0:
                return minutesElapsed
        
        return -1






        

       