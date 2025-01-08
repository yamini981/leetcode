class MedianFinder:

    # we need O(1) access
    # we need to keep the structure sorted (O(1) insertion)
    # thinking ordered map with frequencies?
    # Hashset with frequencies - adding Number would be O(1)

    # I don't think this is possible so what should be sacrificed?
        # could maybe combine two data structures?
    # I think ordered is necessary for median... otherwise we'd have to sort it which is just bad
    # could be tree?
    def __init__(self):
        # two heaps, small and large
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) # -1 to make it a max heap

        # make sure every element is <= every element in large (move from small to large if not)
        if (self.small and self.large and 
            (self.small[0] * -1 > self.large[0])):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # what if the size is uneven?

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1 )


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]

        return (self.small[0]*-1 + self.large[0]) / 2
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()