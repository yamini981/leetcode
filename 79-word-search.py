class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, charSearchIndex):
            
            currChar = word[charSearchIndex]
            if (i < 0 or i >= len(board)
                or j < 0 or j >= len(board[0])
                or board[i][j] != currChar):
                return False
            if charSearchIndex == len(word) - 1:
                return True
                
            board[i][j] = "#"
            if (dfs(i + 1, j, charSearchIndex + 1)
            or dfs(i - 1, j, charSearchIndex + 1)
            or dfs(i, j + 1, charSearchIndex + 1)
            or dfs(i, j - 1, charSearchIndex + 1)):
                return True
            
            board[i][j] = currChar
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (dfs(i, j, 0)):
                    return True

        return False

    


