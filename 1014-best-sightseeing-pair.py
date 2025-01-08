class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best = 0
        i = 0
        for j in range(1, len(values)):
            currScore = values[i] + values[j] + i - j
            best = max(currScore, best)
            if values[j] >= values[i] + i - j:
                i = j
        return best