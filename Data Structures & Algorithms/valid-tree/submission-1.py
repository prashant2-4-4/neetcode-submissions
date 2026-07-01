from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for val in edges:
            adj_list[val[0]].append(val[1])
            adj_list[val[1]].append(val[0])
        
        visited =set()

        def dfs(prev , curr):
            
            if curr in visited:
                return False

            visited.add(curr)
            for neigh in adj_list[curr]:
                if neigh != prev:
                    if not dfs(curr , neigh):
                        return False

            return True      

        
        return dfs(-1 , 0) and n == len(visited)
        