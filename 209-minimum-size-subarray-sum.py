class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # looks like standard sliding window here
        # if you're bigger than the target OR even equal to the target, increment left pointer
        # if you're less than the target, incremetn right pointer

        l,r = 0, 0
        currSum = nums[l]
        minLen = len(nums) + 1

        while r < len(nums):
            if currSum < target:
                r += 1
                if r >= len(nums):
                    break
                currSum += nums[r]
            elif currSum >= target:
                minLen = min(minLen, r - l + 1)
                currSum -= nums[l]
                l += 1
        
        if minLen == len(nums) + 1:
            return 0
        else:
            return minLen
        