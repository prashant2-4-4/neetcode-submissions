class Solution:
    def countBits(self, n: int) -> List[int]:

        def bits(k):
    
            res = 0
            while k:
                res += k % 2
                k = k >> 1
            
            return res
        
        out = [0]

        for i in range(1 , n+1):
            out.append(bits(i))
        return out