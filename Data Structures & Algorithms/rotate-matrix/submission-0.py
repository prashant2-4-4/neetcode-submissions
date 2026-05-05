import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # matrix  = np.array(matrix)
        n = len(matrix)
        # # slicing does not work like that in python list but work in numpu
        # # last_col_store = matrix[: , -1]
        # last_col_store = [col[-1] for col in matrix]
        # print(last_col_store)
        # # iteration over every row
        # for i in range(n):
        #     for j in range(n):
        #         matrix[j][n-i-1] = matrix[i][j]
        #     matrix[n-1][n-i-1] = last_col_store[i]
        #     print(matrix)

        # simple way to rotate transpose and reverse
        for i in range(n):
            for j in range(i+1 , n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
            
        for row in matrix:
            row.reverse()
        