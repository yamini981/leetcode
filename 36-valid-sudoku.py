class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # can just iterate through each rule 1 by 1 ..?

        # iterate through rows
        for row in board:
            unique = set()
            for item in row:
                if item in unique:
                    return False
                if item != ".":
                    unique.add(item)
        
        # iterate through cols
        for j in range(9):
            unique = set()
            for i in range(9):
                item = board[i][j]
                if item in unique:
                    return False
                if item != ".":
                    unique.add(item)

        # x y is coords of top left of box
        def checkSquare(x, y):
            unique = set()
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    item = board[i][j]
                    if item in unique:
                        return False
                    if item != ".":
                        unique.add(item)
            return True
        
        return (checkSquare(0, 0) and checkSquare(3, 0) and checkSquare(6, 0) and
                checkSquare(0, 3) and checkSquare(3, 3) and checkSquare(6, 3) and
                checkSquare(0, 6) and checkSquare(3, 6) and checkSquare(6, 6))

            
