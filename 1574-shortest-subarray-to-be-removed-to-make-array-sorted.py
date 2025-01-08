class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        left = 0

        while left + 1 < len(arr) and arr[left] <= arr[left +1]:
            left += 1

        if left == len(arr) -1:
            return 0

        right = len(arr) -1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        result = min(len(arr) - left -1, right)

        i, j = 0, right
        while i <= left and j < len(arr):
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1

        return result

        


