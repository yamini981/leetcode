class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        # 1  2 3 4
        # 1  1 2  6
        #  24  12  8 6

        curr = 1
        for i in range(1, len(nums)):
            curr *= nums[i-1]
            output[i] *= curr
        
        curr = 1
        for i in range(len(nums) -2, -1, -1):
            curr *= nums[i + 1]
            output[i] *= curr

        return output