class Solution:
    def countBits(self, n: int) -> List[int]:

        def bits(k):
            # k = int(k) # convert to base ten
            res = 0
            while k:
                res += k % 2
                k = k >> 1
            
            return res
        
        out = [0]

        for i in range(1 , n+1):
            # out.append(bits(bin(i)[2:]))
            out.append(bits(i))
        return out