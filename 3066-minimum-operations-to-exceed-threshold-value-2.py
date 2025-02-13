class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # minHeap to keep track of min elements
        numOps = 0
        heapq.heapify(nums)
        while len(nums) >= 2:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            if x >= k and y >= k:
                return numOps

            # x always > y
            heapq.heappush(nums, x * 2 + y)
            numOps += 1
        return numOps