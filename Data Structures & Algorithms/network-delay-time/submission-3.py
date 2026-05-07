from collections import defaultdict
import heapq
class Solution:
    # def dfs(self , nod):
        
    #     if len(self.res) == self.n:
    #         self.cost_lst.append(self.cost)
    #         # return True

    #     # if not self.node[nod]:
    #     #     print('ge')
    #     #     return False
        
    #     for val , co in self.node[nod]:
    #         self.res.append(val)
    #         self.cost += co
    #         # print(self.cost , self.res)
    #         self.dfs(val)
    #         self.res.remove(val)
    #         self.cost -= co
    #         # print('break')
    #         # print(self.cost , self.res)
        
    #     return False



    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # self.node = defaultdict(list)
        # self.res = [k]
        # self.n = n
        # self.cost = 0
        # self.cost_lst = []
        # for u , v , t in times:
        #     self.node[u].append((v,t))

        # self.dfs(k)
        # return min(self.cost_lst) if self.cost_lst else -1

        #dikstra alog

        graph = defaultdict(list)
        heap = [(0 , k)]
        visited = set()
        dist = {}

        for u , v , t in times:
            graph[u].append((v,t))

        while heap:
            cost , node = heapq.heappop(heap)
            if node in visited:
                continue
            
            visited.add(node)
            dist[node] = cost

            for neig , edge_cost in graph[node]:
                if neig not in visited:
                    heapq.heappush(heap , ((cost + edge_cost) , neig))
        
        return max(dist.values()) if len(dist)==n else -1
            

