class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # thinking of doing 4 pointers - one pointer on the left side to know where to place new values,
        # then 3 pointers on the right - start with l = 2, r1,r2,r3 = 0,1,2
        # then while r3 == r2 == r1, do not increment l, do not increment r2 and r1, do not update value at l, just increment r3
        # then, while r3 != r2 and r1, set char[l] = char[r3], and increment l by 1. Set r1 = r2, r2 = r3, r3 = r3 + 1

        #       i
        # 0  0  1  1  2  3  4  4  4
        #       l
        
        # 4 pointers doesn't work - or maybe it does and i couldn't find the edge case idk i got close - in an interview
        # they would have helped me out with a micro hint
        l = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[l - 2]:
                nums[l] = nums[i]
                l += 1

        return l
            