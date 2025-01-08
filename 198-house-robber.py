class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = nums[i] + max(dp[i +2], dp[i + 3])
        # is dp necessary?

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        length = len(nums)
        
        three = nums[length - 1]
        two = nums[length - 2]
        one = nums[length - 3] + three
        zero = 0

        for i in range(length - 4, -1, -1):
            zero = nums[i] + max(two, three)
            three = two
            two = one
            one = zero
        
        return max(one, two)

        # three two one zero
        #   3    10  10   10