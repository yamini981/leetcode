class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        currNums = {}
        l = 0
        r = k - 1
        duplicates = {}
        currSum = 0
        bestSum = 0
        for i in range(0, k):
            if nums[i] in currNums:
                duplicates[nums[i]] = duplicates.get(nums[i], 0) + 1
            currNums[nums[i]] = currNums.get(nums[i], 0) + 1
            currSum += nums[i]
        

        for _ in range(k, len(nums)):
            if not duplicates:
                # print(currSum)
                # print (nums[l:r])
                bestSum = max(bestSum, currSum)
            if nums[l] in duplicates:
                duplicates[nums[l]] -= 1
                if duplicates[nums[l]] == 0:
                    duplicates.pop(nums[l])
            if nums[l] in currNums:
                currNums[nums[l]] -= 1
                if currNums[nums[l]] == 0:
                    currNums.pop(nums[l])
            
            r += 1
            if nums[r] in currNums:
                currNums[nums[r]] += 1
                duplicates[nums[r]] = duplicates.get(nums[r], 0) + 1
            else:
                currNums[nums[r]] = 1
            currSum = currSum + nums[r] - nums[l]
            l += 1
        
        if not duplicates:
            bestSum = max(currSum, bestSum)

        return bestSum
            
            

