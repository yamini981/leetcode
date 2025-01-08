class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # sliding window with removing from set
        l = 0
        potentialDuplicates = set()
        k = min(k, len(nums))
        for i in range(k):
            if nums[i] in potentialDuplicates:
                return True
            potentialDuplicates.add(nums[i])
        
        for r in range(k, len(nums)):
            if nums[r] in potentialDuplicates:
                return True

            potentialDuplicates.add(nums[r])
            potentialDuplicates.remove(nums[l])
            l += 1
        return False
