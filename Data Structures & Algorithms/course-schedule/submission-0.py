# topological sort , kahn's algo , this problem can also be solve if their loop return false else true
from collections import defaultdict , deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # indegree = defaultdict(int)
        indegree = [0]*numCourses
        graph = defaultdict(list)
        for a , b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        visited = 0
        while queue:
            node = queue.popleft()
            visited += 1

            for u in graph[node]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    queue.append(u)
        
        return visited == numCourses

        