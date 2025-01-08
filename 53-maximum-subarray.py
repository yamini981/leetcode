class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Feels like sliding window type of thing...
        # Start with L = 0, R = 1, currTotal = nums[0], newTotal = nums[L] + nums[R]
        # best = max(currTotal, newTotal)
        # if currTotal < 0 OR nums[L] < 0: shift Left 
            # don't let left surpass right
        # otherwise, shift the right (?)

        curSum = 0
        best = nums[0]

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            best = max(curSum, best)
        
        return best
                