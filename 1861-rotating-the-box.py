class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Reconstruct the box after rotating 90 degrees
        # have each stone fall starting at the bottom of the box until the end of the box
        # or obstacle or stone (stone is okay because there should only be stones at the bottom under)

        m = len(box)
        n = len(box[0])
        newBox = [[0]*m for _ in range(n)] 

        # rotate 90 degrees clockwise
        for i in range(m):
            for j in range(n):
                newBox[j][m - 1 - i] = box[i][j]
        
        # newBox is n x m now
        for i in range(len(newBox) - 1, -1, -1):
            for j in range(len(newBox[0])):
                if newBox[i][j] == '#':
                    nextDown = i + 1
                    while nextDown < len(newBox):
                        if newBox[nextDown][j] == '*' or newBox[nextDown][j] == '#':
                            break
                        newBox[nextDown - 1][j] = '.'
                        newBox[nextDown][j] = '#'
                        nextDown += 1

        return newBox