import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x , y in points:
            dist = (x**2 + y**2) ** 0.5
            heapq.heappush(heap , (-dist , [x , y]))
            if len(heap) > k:
                heapq.heappop(heap)
        # out = []
        # while k:
        #     out.append(heap[0][1])
        #     heapq.heappop(heap)
        #     k -= 1
        out = [x[1] for x in heap[:k]]
        return out