from collections import defaultdict , deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i , eq in enumerate(equations):
            a , b = eq
            graph[a].append((b , values[i]))
            graph[b].append((a , 1/values[i]))
        
        # print(adj_lst)
        visited = set()
        queue = deque()
        ans = []
        for query in queries:
            start , target = query

            min_cost = float("inf")
            visited = set()
            queue = deque()

            queue.append((start , 1))
            visited.add(start)
            if start not in graph or target not in graph:
                ans.append(-1)
                continue

            while queue:
                node,cost = queue.popleft()
                if node==target:
                    ans.append(cost)
                    break

                for nei in graph[node]:
                    if nei[0] not in visited:
                        queue.append((nei[0] , cost * nei[1]))
                        visited.add(nei[0])
            
            else:
                ans.append(-1)
        

        return ans




        