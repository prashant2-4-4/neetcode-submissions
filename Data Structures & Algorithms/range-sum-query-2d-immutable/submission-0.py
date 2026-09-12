class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.prefix = [[0 for _ in range(self.col+1)] for _ in range(self.row+1)]
        # print(self.prefix)
        for r in range(self.row):
            for c in range(self.col):
                self.prefix[r+1][c+1] = (matrix[r][c] + self.prefix[r][c+1] + self.prefix[r+1][c]  - self.prefix[r][c]) 

        # for r in range(self.row):
        #     for c in range(1 , self.col):
        #         self.matrix[r][c] += self.matrix[r][c-1]
        
        # for c in range(self.col):
        #     for r in range(1 , self.row):
        #         self.matrix[r][c] += self.matrix[r-1][c]
        
        print(self.prefix)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix[row2+1][col2+1] 
        + self.prefix[row1][col1]
         - self.prefix[row2+1][col1]
         -self.prefix[row1][col2+1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)