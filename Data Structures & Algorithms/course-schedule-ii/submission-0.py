from collections import defaultdict , deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort , kahn's algo , this problem can also be solve if their loop return false else true

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
        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)

            for u in graph[node]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    queue.append(u)
        
        return topo if len(topo) == numCourses else []

        
        