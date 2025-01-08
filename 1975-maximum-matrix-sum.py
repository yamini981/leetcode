class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # don't you just minimize the negatives?
        # Find a negative, then find the adjacent numbers - 
        # multiply by the adjacent smallest number
        # or if the maginuted of the negative is smaller than all of the surroudning positive,
        # do not multiply by -1
        # or we could just brute force by trying every combination... actually that would be ass
        # maybe only check down and right..?
        numNegatives = 0
        smallestNum = 100001
        smallestNumCoords = [-1, -1]
        for i in range(len(matrix)):    
            for j in range(len(matrix[0])):
                curr = matrix[i][j]
                magCurr = abs(curr)
                if magCurr < smallestNum:
                    smallestNum = magCurr
                    smallestNumCoords = [i, j]
                if curr <= 0:
                    numNegatives += 1

        total = 0
        if numNegatives % 2 == 0:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    total += abs(matrix[i][j])
        else:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i == smallestNumCoords[0] and j == smallestNumCoords[1]:
                        if matrix[i][j] > 0:
                            total -= matrix[i][j]
                        else:
                            total += matrix[i][j]
                    else:
                        total += abs(matrix[i][j])
        return total
                    