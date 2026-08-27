from collections import defaultdict , deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_lst = defaultdict(list)

        for i , eq in enumerate(equations):
            a , b = eq
            adj_lst[a].append((b , values[i]))
            adj_lst[b].append((a , 1/values[i]))
        
        # print(adj_lst)
        visited = set()
        queue = deque()
        ans = []
        for query in queries:
            a , b = query

            min_cost = float("inf")
            visited = set()
            queue = deque()

            queue.append((a , 1))
            visited.add(a)
            while queue:
                stage,cost = queue.popleft()
                for val in adj_lst[stage]:
                    if val[0] == b:
                        min_cost = cost * val[1]
                        break
                    else:
                        if val[0] not in visited:
                            queue.append((val[0] , cost * val[1]))
                            visited.add(val[0])
            ans.append(-1 if min_cost == float("inf") else min_cost)
        

        return ans




        