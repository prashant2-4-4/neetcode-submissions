from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # detecting cycle and implemting dsu(union find algo)
        # rank by size and not by rank
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1]*(n+1)

        def find(x):
            if x == parent[x]:
                return parent[x]
            
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(n1 , n2):
            p1 , p2 = find(n1) , find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True
        
        for n1,n2 in edges:
            if not union(n1 , n2):
                return [n1 , n2]


        