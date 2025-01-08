class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # sorting would make for a fairly simple O(nlogn solution)
        # if you don't sort, you'd have to do O(n * k) since 
        # you have multiple shifts... I guess sorting is best

        # 2 POINTER!!

        k = 0

        for i in range(len(nums)):
            if val != nums[i]:
                nums[k] = nums[i]
                k += 1
        
        return k
            



        

        