class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def checkLiveNeighbors(i, j):
            numLive = 0
            # [i + 1][j]
            if i + 1 < m:
                if board[i + 1][j] == 1 or board[i + 1][j] == 3:
                    numLive += 1
            # [i][j + 1]
            if j + 1 < n:
                if board[i][j + 1] == 1 or board[i][j + 1] == 3:
                    numLive += 1
            # [i - 1][j]
            if i - 1 >= 0:
                if board[i - 1][j] == 1 or board[i - 1][j] == 3:
                    numLive += 1
            # [i][j - 1]
            if j - 1 >= 0:
                if board[i][j-1] == 1 or board[i][j-1] == 3:
                    numLive += 1
            # [i + 1][j + 1]
            if i + 1 < m and j + 1 < n:
                if board[i + 1][j + 1] == 1 or board[i + 1][j + 1] == 3:
                    numLive += 1
            # [i + 1][j - 1]
            if i + 1 < m and j - 1 >= 0:
                if board[i + 1][j - 1] == 1 or board[i + 1][j - 1] == 3:
                    numLive += 1
            # [i - 1][j + 1]
            if i - 1 >= 0 and j + 1 < n:
                if board[i - 1][j + 1] == 1 or board[i -1][j + 1] == 3:
                    numLive += 1
            # [i - 1][j - 1]
            if i - 1 >= 0 and j - 1 >= 0:
                if board[i -1][j -1] == 1 or board[i -1][j -1] == 3:
                    numLive += 1

            return numLive

        for i in range(m):
            for j in range(n):
                numLiveNeighbors = checkLiveNeighbors(i, j)
                currValue = board[i][j]
                if currValue == 1:
                    if numLiveNeighbors < 2 or numLiveNeighbors > 3:
                        board[i][j] = 3
                if currValue == 0:
                    if numLiveNeighbors == 3:
                        board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
        