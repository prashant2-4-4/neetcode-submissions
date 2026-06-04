class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = set()
        def dfs(i ,j , idx):
            if idx == len(word):
                return True
            if i >= row or i < 0 or j >= col or j < 0:
                return False
            
            if board[i][j] != word[idx]:
                return False


            if (i , j) in visited: # cannot use same cell
                return False

            visited.add((i,j))

            for dir_x , dir_y in [[-1 , 0] , [0 , -1] , [1 , 0] , [0 , 1]]:
                if dfs(i+dir_x , j + dir_y , idx+1):
                    return True
            
            visited.remove((i,j)) # backtrack now you can use

        
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(i , j , 0):
                        return True
        
        return False
                
        