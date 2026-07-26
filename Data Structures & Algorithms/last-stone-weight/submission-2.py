import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        #O(nlogn)
        # for stone in stones:
        #     heapq.heappush(heap , -stone)
        heap = [-stone for stone in stones] #O(n)
        heapq.heapify(heap) #O(n)
        
        while len(heap) > 1:
            a = heapq.heappop(heap) #logn
            b = heapq.heappop(heap) #logn
            if a == b:
                continue
            else:
                heapq.heappush(heap , -abs(a-b))

        return -heap[0] if heap else 0       