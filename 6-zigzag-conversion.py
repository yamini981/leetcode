class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        mylist = [""] * numRows
        row = 0
        moveDown = True
        for char in s:
            mylist[row] += char
            if row == numRows - 1:
                moveDown = False
            if row == 0:
                moveDown = True
            if moveDown:
                row += 1
            else:
                row -= 1
        
        ret = ""
        for string in mylist:
            ret += string

        return ret