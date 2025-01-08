class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        if s[0] == '0':
            score += 1
        
        for i in range(1, len(s)):
            if s[i] == '1':
                score += 1
        
        bestScore = score

        for split in range(1, len(s) - 1):
            if s[split] == '0':
                score += 1
            else:
                score -= 1
            bestScore = max(score, bestScore)
        
        return bestScore