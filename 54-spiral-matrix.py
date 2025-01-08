class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        left, top = 0, 0
        right, bottom = len(matrix[0]) - 1, len(matrix) - 1
        matrixSize = len(matrix) * len(matrix[0])
        i, j = 0, 0

        while len(res) < matrixSize:
            #go right until right border, update top border
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            #go down until bottom border, update right border
            for j in range(top, bottom + 1):
                res.append(matrix[j][right])
            right -= 1
            if len(res) >= matrixSize:
                break
            #go left until left border, update bottom border
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            #go up until top border, update left border
            for j in range(bottom, top - 1, -1):
                res.append(matrix[j][left])
            left += 1

        return res
