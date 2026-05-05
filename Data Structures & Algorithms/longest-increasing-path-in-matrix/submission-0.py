class Solution:

    def valid(self , i , j ):
        if 0 <= i < self.row and 0 <= j < self.col:
            return True
        
        return False

    def dfs(self , i , j):
        if (i , j) in self.memo:
            return self.memo[(i , j)]

        best = 1

        for dx , dy in [(i-1 , j) ,(i+1 , j) , (i , j -1) , (i , j + 1)]:
            if self.valid(dx , dy) and self.matrix[dx][dy] > self.matrix[i][j]:
                best = max(best , 1 + self.dfs(dx , dy))
        
        self.memo[(i , j)] = best
        return best

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        result = 0
        self.row , self.col = len(matrix) , len(matrix[0])
        self.memo = {}
        self.matrix = matrix

        for i in range(self.row):
            for j in range(self.col):
                result = max(result , self.dfs(i , j))
        
        return result
                


        
        # max_len = 0
        # row = len(matrix)
        # col = len(matrix[0])
        # res = 0
        # for i in range(row):
        #     for j in range(col):
        #         res = self.recursion(0 , i , j , matrix , 0)
        #         max_len = max(res , max_len)

        # return max_len 
        