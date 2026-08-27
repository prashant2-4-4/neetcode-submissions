# O(n α(n))

# Since inverse Ackermann α(n) grows ridiculously slowly:

# α(n) ≈ constant

# so in interviews you can say:

# Time: O(n α(n)) ≈ O(n)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        size = [1] * (n+1)
        parent = [i for i in range(n+1)]

        # finding group in which it belongs
        def find(x):
            if parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
        
        
        def union(n1 , n2):
            p1 , p2 = find(n1) , find(n2)
            #belonging same group , adding them will cause cycle
            if p1 == p2:
                return False
            
            if size[p1] > size[p2]:
                parent[p2] = p1 #smaller parent will go into larger parent
                size[p1] += size[p2]
            
            else:
                parent[p1] = p2
                size[p2] += size[p1]

            return True


        for n1 , n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        