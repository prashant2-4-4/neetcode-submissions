from collections import Counter , deque
import heapq
# https://claude.ai/chat/f541d6a3-e165-40d6-bf69-7c63f64920a5
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [] # store most frequent element
        queue = deque() # tuple of  (task , time)
        for key , value in count.items():
            heapq.heappush(heap , (-value , key)) 
        # print(heap)
        step = 0
        while heap or queue:
            step += 1
            if not heap and queue: 
                step = queue[0][0]
        
            
            # check if decrement task present in queue
            if queue and queue[0][0] == step:
                t , key , val = queue.popleft()
                heapq.heappush(heap , (-val , key))
            
            # now update heap
            if heap:
                val , key = heapq.heappop(heap)
                val = -1 * val

                val -= 1
                if val > 0:
                    queue.append((step + n + 1 , key , val))
            


        return step




