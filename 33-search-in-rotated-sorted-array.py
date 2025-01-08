class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Track left pointer, right pointer, and then the middle of them
        # 4 5 6 7 0 1 2
        # L     M     R
        # if L < M and target between L and M:
        #       r = mid
        # if R > M and target between M and R:
        #       l = mid
        # if R < M and target < R:
        #       l = mid
        # if L > M and target > L:
        #       r = mid

        l, r = 0, len(nums) - 1



        while l <= r:
            m = (l + r) // 2
            if nums[l] == target:
                return l
            if nums[m] == target:
                return m
            if nums[r] == target:
                return r

            # 7 8 1 2 3 4 5 6
           
            if target > nums[l] and target < nums[m] and nums[l] < nums[m]:
                l += 1
                r = m - 1
            elif (target > nums[l] or target < nums[m]) and nums[l] > nums[m]:
                l += 1
                r = m -1
            elif target < nums[r] and target > nums[m] and nums[r] > nums[m]:
                l = m + 1
                r -= 1
            elif (target < nums[r] or target > nums[m]) and nums[r] < nums[m]:
                l = m + 1
                r -= 1
            else:
                return -1
        
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1


            