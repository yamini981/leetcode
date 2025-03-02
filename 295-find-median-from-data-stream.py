class MedianFinder:

    def __init__(self):
        self.numElements = 0
        self.minHeap = []
        self.maxHeap = []
        self.currMedian = None
    def addNum(self, num: int) -> None:
        if self.numElements == 0:
            self.minHeap.append(num)
            self.currMedian = num
        else:
            if num <= self.currMedian:
                # add to maxHeap, but what if maxHeap is bigger then minHeap?
                # we need to pop from maxHeap and add to minHeap then push new val
                # onto maxHeap
                if len(self.maxHeap) == len(self.minHeap):
                    heapq.heappush(self.maxHeap, -1 * num)
                    self.currMedian = -1*self.maxHeap[0]
                elif len(self.maxHeap) < len(self.minHeap):
                    heapq.heappush(self.maxHeap, -1 * num)
                    self.currMedian = (-1*self.maxHeap[0] + self.minHeap[0]) / 2
                elif len(self.maxHeap) > len(self.minHeap):
                    poppedMax = heapq.heappop(self.maxHeap) * -1
                    heapq.heappush(self.minHeap, poppedMax)
                    heapq.heappush(self.maxHeap, -1 * num)
                    self.currMedian = (-1*self.maxHeap[0] + self.minHeap[0]) / 2
            else:
                # add to minHeap, but what if minHeap is longer than maxHeap?
                # need to pop from minHeap and add to maxHeap then push new val
                # onto minHeap
                if len(self.maxHeap) == len(self.minHeap):
                    heapq.heappush(self.minHeap, num)
                    self.currMedian = self.minHeap[0]
                elif len(self.minHeap) < len(self.maxHeap):
                    heapq.heappush(self.minHeap, num)
                    self.currMedian = (-1*self.maxHeap[0] + self.minHeap[0]) / 2
                elif len(self.minHeap) > len(self.maxHeap):
                    poppedMin = heapq.heappop(self.minHeap)
                    heapq.heappush(self.maxHeap, -1*poppedMin)
                    heapq.heappush(self.minHeap, num)
                    self.currMedian = (-1*self.maxHeap[0] + self.minHeap[0]) / 2
        self.numElements += 1


        

    def findMedian(self) -> float:
        return self.currMedian
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()