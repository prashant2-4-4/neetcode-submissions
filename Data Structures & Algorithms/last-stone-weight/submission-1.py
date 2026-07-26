import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for stone in stones:
            heapq.heappush(heap , -stone)
        
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            if a == b:
                continue
            else:
                heapq.heappush(heap , -abs(a-b))

        return -heap[0] if heap else 0       