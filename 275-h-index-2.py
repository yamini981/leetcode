# NOT OPTIMAL!
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Wait this is wrong I need to do some binary search shit
        # figure out later
        bestHindex = 0
        for i in range(len(citations)):
            # number of papers with current citation num or better
            numAhead = len(citations) - i
            bestHindex = max(bestHindex, min(numAhead, citations[i]))
        return bestHindex