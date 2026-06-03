import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for nu in nums:
            if len(heap) < k:
                heapq.heappush(heap , nu)
            
            elif nu > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap , nu)
            else:
                pass
        
        return heap[0]
