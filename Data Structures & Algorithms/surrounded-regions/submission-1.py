from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        row , col = len(board) , len(board[0])
        visited = set()
        for r in range(row):
            if board[r][0] == 'O':
                queue.append((r,0))
                visited.add((r,0))
            
            if board[r][col-1] == 'O':
                queue.append((r,col-1))
                visited.add((r,col-1))
            
        for c in range(col):
            # print(board[row-1][c])
            if board[0][c] == 'O':
                queue.append((0 , c))
                visited.add((0,c))
            
            if board[row-1][c] == "O":
                # print('her')
                queue.append((row-1 , c))
                visited.add((row-1 , c))
        
        directions = [[-1 ,0] , [1 , 0] , [0 , -1] , [0 , 1]]
        print(visited)
        while queue:
            r,c = queue.popleft()

            for dir_x , dir_y in directions:
                rx = r + dir_x
                cy = c + dir_y

                if rx >= 0 and rx < row and cy >= 0 and cy < col and (rx,cy) not in visited and board[rx][cy] == 'O':
                    # print('here')
                    # print(rx , cy , r , c)
                    visited.add((rx , cy))
                    queue.append((rx , cy))
        
        print(visited)
        for r in range(row):
            for c in range(col):
                if (r,c) not in visited and board[r][c]=='O':
                    board[r][c] = 'X'
                

            
