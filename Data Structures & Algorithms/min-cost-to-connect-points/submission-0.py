from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        adj_list = defaultdict(list)
        
        for i in range(n):
            x1 , y1 = points[i]

            for j in range(i+1 , n):
                x2 , y2 = points[j]
                adj_dis = abs(x2 - x1) + abs(y2 - y1)
                adj_list[i].append([adj_dis , j])
                adj_list[j].append([adj_dis , i])
        # print(adj_list)

        res = 0
        minheap = [(0 , 0)]
        visited = set()
        while n != len(visited):
            cost , loc = heapq.heappop(minheap)
            if loc in visited:
                continue
            res += cost
            visited.add(loc)
            for co , lo in adj_list[loc]:
                heapq.heappush(minheap , (co , lo))
        return res



        