class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # sliding window!
        l = 0
        r = 1
        bestSum = nums[l]
        currSum = nums[l]
        # 10 9 8 7
        while r < len(nums):
            print(currSum)
            if nums[r] > nums[r - 1] or l == r:
                currSum += nums[r]
                r += 1
            else:
                currSum -= nums[l]
                l += 1

            bestSum = max(currSum, bestSum)

        return bestSum