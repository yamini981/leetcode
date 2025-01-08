class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window
        l, r = 0, 0
        best = len(nums) + 1
        currTotal = 0
        changeR = True

        while r < len(nums):
            if changeR:
                currTotal += nums[r]
            if currTotal >= target:
                if r == l:
                    return 1
                best = min(best, r - l + 1)
                currTotal -= nums[l]
                l += 1
                changeR = False
            else:
                r += 1
                changeR = True

        if best == len(nums) + 1:
            return 0
        else:
            return best
            
