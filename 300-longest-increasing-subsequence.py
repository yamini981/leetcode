class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Thinking DP of some kind
        # So for example, start at last number: answer is dp[last] = 1
        # if nums[i] < nums[i + 1]:
        #     dp[i] = dp[i + 1] + 1
        # else:
        #     dp[i] = dp[i + 1]

        dp = [1] * len(nums)
        for i in range(len(nums) -2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    

        return max(dp)