class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # idea is iterate through the list, and if the new value is bigger than the last value, we pop the last value
        # then after popping a bunch of times we add to the end of the list
        
        # as we're going through the list of numbers, we always start by doing the popping the last value thing if the 
        # current number is bigger, then we check if the index at the front of our queue is valid or not
        # if it's valid, add that to the answer, if not, pop it and get the next one

        ans = []
        dq = deque()

        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        ans.append(nums[dq[0]])

        for i in range (k, len(nums)):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if dq[0] == i - k:
                dq.popleft()
            ans.append(nums[dq[0]])
        return ans

        
