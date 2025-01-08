class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # I'm thinking sliding window: l = 0, r = k
        # manually check if first window is in order
        # KEY IS SLIDING WINDOW, KEEP TRACK OF NUMBER OF CONSECUTIVE!
        res = []
        l = 0
        consecutive_count = 1
        for r in range(len(nums)):
            if r > 0 and nums[r -1] + 1 == nums[r]:
                consecutive_count += 1
            if r - l + 1 > k:
                if nums[l] + 1 == nums[l + 1]:
                    consecutive_count -= 1
                l += 1
            
            if r -l + 1 == k:
                if consecutive_count == k:
                    res.append(nums[r])
                else:
                    res.append(-1)
            
        return res

            


        # n = len(nums)
        
        # currSubArray = nums[0:k]
        

        # for i in range(k, len(nums) + 1):
        #     currSubArray = nums[i - k:i]
        #     print(currSubArray)
        #     for j in range(len(currSubArray) - 1):
        #         c = currSubArray[j]
        #         n = currSubArray[j + 1]

        #         if c != n - 1:
        #             res[i - k] = -1
        #             break
        #     if res[i - k] == -2:
        #         res[i - k] = currSubArray[k - 1]

        # return res

