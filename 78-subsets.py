class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for each number, we either use it as a set,
        # or we create a new set by appending it onto an existing set

        ans = [[]]
        for num in nums:
            for i in range(len(ans)):
                newArr = copy.copy(ans[i])
                newArr.append(num)
                ans.append(newArr)
        return ans
