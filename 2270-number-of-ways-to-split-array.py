class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        numWays = 0
        leftSum = 0
        rightSum = sum(nums)
        
        for k in range(len(nums) - 1):
            leftSum += nums[k]
            rightSum -= nums[k]
            if leftSum >= rightSum:
                numWays += 1
        return numWays