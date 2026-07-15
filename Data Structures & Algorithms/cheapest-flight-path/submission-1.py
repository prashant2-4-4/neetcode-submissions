from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for flight in flights:
            graph[flight[0]].append((flight[1] , flight[2]))
        
        visited = {}
        def dfs(curr , stop):
            if (curr , stop) in visited:
                return visited[(curr,stop)]

            if curr == dst:
                return 0
            
            if stop > k:
                return float("inf")

            best = float("inf")
            for nxt_stop , travel_cost in graph[curr]:
                res = dfs(nxt_stop , stop+1) + travel_cost
                if res != float("inf"):
                    best = min(best , res)
            
            visited[(curr , stop)] = best

            return visited[(curr , stop)]
            

        ans = dfs(src , 0)
        return -1 if ans==float('inf') else ans