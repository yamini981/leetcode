class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""
        for i in range(len(nums)):
            if nums[i][i] == '1':
                ans += '0'
            else:
                ans += '1'
        return ans