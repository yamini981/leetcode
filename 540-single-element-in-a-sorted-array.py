class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # definitely a variant of binary search
        # wait no... hold on... sorted only guarantees that the duplicate
        # numbers are right next to each other

        # we know the length is always gonna be odd... how could this be O(logn)?

        # ok hold on... so if we scan 2 numbers in the middle
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (r + l) // 2
            midEven = mid % 2 == 0

            if midEven:
                if mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                    l = mid + 1
                elif mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                    
                    r = mid - 1
                else:
                    return nums[mid]
            else:
                if mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                    r = mid - 1
                elif mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                    l = mid + 1
                else:
                    return nums[mid]
        return nums[l]