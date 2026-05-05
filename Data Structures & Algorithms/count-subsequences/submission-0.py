class Solution:

    # def recursion(self , st , itera) --> int:
    #     if st == self.t:
    #         return 1
        
    #     if st in memo:
    #         return memo[st]

    #     if itera == len(self.s) or len(itera) >= len(t):
    #         return 0

    #     check = self.recursion(st + "" , itera) , self.recursion(st+s[itera] , itera+1)

    
    def recursion(self, i, j):
        # base cases
        if j == len(self.t): return 1 # we exhausted t
        if i == len(self.s): return 0 # we exhausted s but did not find t
        
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        # always can skip s[i]
        # either matches or not
        result = self.recursion(i+1, j)
        
        # if match, can also use s[i]
        if self.s[i] == self.t[j]:
            result += self.recursion(i+1 , j+1)
        
        self.memo[(i, j)] = result
        return result

    def numDistinct(self, s: str, t: str) -> int:

        count = 0
        self.t = t
        self.s = s
        self.memo = {}
        
        return self.recursion(0 , 0)
