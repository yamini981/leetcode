class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l = 0
        # r = len(nums) - 1
        # mid = (r - l) // 2

        # 2 3 4 5 6 1
        #       l m r

        # if mid > right, then min is between mid and right
        # if left > mid, then min is between left and mid

        left, right = 0, len(nums) - 1

        while left < right - 1:
            mid = (right + left) // 2

            if nums[left] > nums[mid]: 
                left = left + 1
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return nums[left]
        
        return min(nums[left], nums[right])

