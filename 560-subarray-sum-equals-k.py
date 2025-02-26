class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # uses fact that sum(i, j) = sum(0, j) - sum(0, i-1)
        # or rearranged, cumSum - prevCumSum = k
        # the above equation we should count how many times we can recreate k using cumSum and prevCumSum
        # so we use the number of times we see prevCumSum
        cumSum = 0
        occurences = 0
        mrMap = {}
        
        # this is basically same as saying we have already seen 0, which is true!
        # since that is our starting sum. Allows to check if current cumSum is equal to k
        mrMap[0] = 1
        for num in nums:
            cumSum += num
            occurences += mrMap.get(cumSum - k, 0)
            mrMap[cumSum] = mrMap.get(cumSum, 0) + 1
        
        return occurences
