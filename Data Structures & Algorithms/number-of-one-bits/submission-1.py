class Solution:
    def hammingWeight(self, n: int) -> int:
        # two solutions
        # one is n % 2 and then shift to right >>
        # second is n & (n-1) and add every time you do this operations

        res = 0
        while n:
            #one approach
            # res += n%2
            # n = n >> 1
            # second apprach
            res += 1
            n &= (n-1)
        
        return res
        