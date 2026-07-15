# inplace only first row and columns other wise we can do in place
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        row , col = len(matrix) , len(matrix[0])
        firstrow = False
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:

                    matrix[0][c] = 0

                    if r == 0:
                        firstrow = True
                    
                    else:
                        matrix[r][0] = 0
        
        # print(matrix)

        for r in range(1 , row):
            for c in range(1 , col):
                if matrix[0][c]==0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        print(firstrow)
        #first row

        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0

        if firstrow:
            for c in range(col):
                matrix[0][c] = 0

     

        
        