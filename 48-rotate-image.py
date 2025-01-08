class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        l, r = 0, n-1

        while l < r:
            for i in range (r - l):
                t = l
                b = r
                matrix[t][l+i], matrix[t+i][r] = matrix[t+i][r], matrix[t][l+i]
                matrix[t][l+i], matrix[b][r-i] = matrix[b][r-i], matrix[t][l+i]
                matrix[t][l+i], matrix[b-i][l] = matrix[b-i][l], matrix[t][l+i]

            r -= 1
            l += 1
            

            



        