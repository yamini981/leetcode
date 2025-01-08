class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # sliding window, but have to deal with negative situation...
        # if next value is positive, increase window size to the right
        # if next value is negative, if it makes the product positive, shift right
        # if next value is 0 or end of array, shift left until L = R. (and then R = R+1)
        # n^2 solution easy
        # -2 0 5 5 5 5 5
        #  L R

        res = -11
        curMin, curMax = 1, 1

        for n in nums:

            tmp = curMax
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp * n, curMin * n, n)

            res = max(curMax, res)

        return res

            
