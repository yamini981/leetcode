class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force - manually go through each potential k value from 
        # 1, ceil(piles[i] / k) = numHours for a pile
        # could binary search the k value ..?
    
        lowerBound = 1
        upperBound = max(piles)
        while upperBound != lowerBound:
            k = (upperBound + lowerBound) // 2
            numHours = h
            for pile in piles:
                hoursSpent = math.ceil(pile / k)
                numHours -= hoursSpent
                if numHours < 0:
                    break
            if numHours < 0:
                lowerBound = k + 1
                continue
            upperBound = k
            
        return upperBound
