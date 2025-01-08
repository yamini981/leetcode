class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # only up to 20 numbers, can store the potential sums up to that point?
        # each number can be +/-, so 2^20 options for sums? Maybe some kind of DP is best
        
        totalSum = sum(nums)

        dp = {}
        dp[nums[0] + totalSum] = 1
        dp[-nums[0] + totalSum] = dp.get(-nums[0] + totalSum, 0) + 1
        print(dp)

        for i in range (1, len(nums)):
            next_dp = {}
            for key, val in dp.items():
                next_dp[key + nums[i]] = val + next_dp.get(key + nums[i], 0)
                next_dp[key - nums[i]] = val + next_dp.get(key - nums[i], 0)
            dp = next_dp
        return dp.get(target + totalSum, 0)
