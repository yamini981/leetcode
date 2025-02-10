class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # key: nums[i] - nums[j] != j - i is equivalent to: nums[i] - i != nums[j] - j
        # also, sum of unique pairs = n(n-1)/2
        numSubIndex = {}
        for i in range(len(nums)):
            numSubIndex[nums[i] - i] = numSubIndex.get(nums[i] - i, 0) + 1
       
        numGoodPairs = 0
        for val in numSubIndex.values():
            numPairs = (val) * (val - 1)//2
            numGoodPairs += numPairs

        return (len(nums) * (len(nums) - 1) // 2) - numGoodPairs
