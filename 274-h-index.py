class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # h-index = max value of h such that the
        # the researcher has published at least h papers
        # that have been cited that many times
        # i.e.: h = 3, then they need at least 3 papers that have
        # been cited 3 times

        # easy solution - sort array: but it's O(nlogn)
        
        # citations.sort()
        # bestHindex = 0
        # for i in range(len(citations)):
        #     # number of papers with current citation num or better
        #     numAhead = len(citations) - i
        #     bestHindex = max(bestHindex, min(numAhead, citations[i]))
        # return bestHindex

        # other solution - can also do bucket sort! it's O(n) time but also
        # O(n) space

        bucketList = [0] * (max(citations) + 1)
        for i in range(len(citations)):
            bucketList[citations[i]] += 1

        currCount = 0

        for i in range(len(bucketList) - 1, -1, -1):
            currCount += bucketList[i]

            if currCount >= i:
                return i

        return 0
        