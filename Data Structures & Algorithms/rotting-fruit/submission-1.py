#bfs answer
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
                
                if grid[i][j] == 1:
                    fresh += 1
        
        
        if fresh == 0:
            return 0

        minutes = 0
        directions = [(-1, 0) , (0 , -1) , (1 , 0) , (0 , 1)]

        while queue and fresh:

            for _ in range(len(queue)):
                i , j = queue.popleft()

                for dx , dy in directions:
                    ni = i + dx
                    nj = j + dy

                    if 0 <= ni < row and 0 <= nj < col:
                        if grid[ni][nj] == 1:
                            grid[ni][nj] = 2
                            fresh -= 1
                            queue.append((ni , nj))
                
            minutes += 1
        
        return minutes if not fresh else -1




