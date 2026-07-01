from collections import defaultdict , deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = defaultdict(list)
        
        for edge in edges:

            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        
        visited = set()
        count = 0
        for i in range(n):
            if not i in visited:
                count += 1

                queue = deque()
                queue.append(i)
                visited.add(i)
                while queue:
                    node = queue.popleft()

                    for neigh in adj_list[node]:
                        if neigh not in visited:
                            queue.append(neigh)
                            visited.add(neigh)
        return count
            