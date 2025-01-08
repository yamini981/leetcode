class Solution:
    
    def rob(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        
        def houseRobber(nums):
            if len(nums) == 1:
                return nums[0]

            DP = [None] * len(nums)
            DP[len(nums) - 1] = nums[len(nums) - 1]
            DP[len(nums) - 2] = nums[len(nums) - 2]
            if len(nums) >= 3:
                DP[len(nums) - 3] = nums[len(nums) - 3] + nums[len(nums) - 1]
            
            for i in range(len(nums) - 4, -1, -1):
                DP[i] = max(DP[i+2], DP[i + 3]) + nums[i]
            
            return max(DP[0], DP[1])
        
        return max(houseRobber(nums[1:]), houseRobber(nums[:len(nums) - 1]))
    
    

