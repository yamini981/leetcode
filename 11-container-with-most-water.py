class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer with left on left, right on right

        l, r = 0, len(height) - 1
        best = 0

        while l < r:
            if height[l] < height[r]:
                best = max(best, height[l] * (r - l))
                l += 1
            else:
                best = max(best, height[r] * (r - l))
                r -= 1

        return best
