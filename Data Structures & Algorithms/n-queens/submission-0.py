#backtracking brute force
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_dia = set() # r-c
        neg_dia = set() # r + c
        res = [] #storing all the board
        board = [["." for _ in range(n)] for _ in range(n)] #intial board all empty
        
        def backtrack(row):
            if row==n: # reached end or out of bound
                copy = ["".join(r) for r in board]
                res.append(copy)
                return 

            for col in range(n):
                if col in cols or (row-col) in pos_dia or (row+col) in neg_dia:
                    continue

                board[row][col] = 'Q'
                pos_dia.add(row-col)
                neg_dia.add(row+col)
                cols.add(col)
                backtrack(row+1)

                # change all value to original for next index in columns
                board[row][col] = '.'
                pos_dia.remove(row-col)
                neg_dia.remove(row+col)
                cols.remove(col)
        backtrack(0)
        return res
