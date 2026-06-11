import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap , -num)
        # if len(self.max_heap) >= len(self.min_heap) + 1:
        val = -1 * heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap , val)

        if len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap , -val) 

        

    def findMedian(self) -> float:
        
        if len(self.max_heap) > len(self.min_heap):
            return - self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0])/2

        