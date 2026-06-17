class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1:
            if n in visited:
                return False

            visited.add(n)

            new_n = str(n)
            add_n = 0
            for i in new_n:
                i = int(i)
        
                add_n += (i*i)
         
            n = add_n

        
        return True
        