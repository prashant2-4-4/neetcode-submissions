from collections import deque
class Solution:
    #     self.memo = {}

    #     for i in range(self.row):
    #         for j in range(self.col):
    #             self.count = 0
    #             if grid[i][j] in {-1 , 0}:
    #                 pass
    #             else:
    #                 grid[i][j] = self.dfs(i , j)
    # def dfs(self , i : str , j : str) -> int:

    #     if self.row <= i <-1 and self.col <= j < -1:
    #         return 0
    #     if self.grid[i][j] == 0:
    #         return self.count
    #     if self.grid[i][j] == -1:
    #         return 0

    #     if (i,j) in self.memo:
    #         return self.memo[(i,j)]
        
    #     self.count += 1
    #     self.count += max(self.dfs(i-1 , j) , self.dfs(i+i ,j) , self.dfs(i , j-1) , self.dfs(i , j+1))
        
    #     self.memo[(i,j)] = self.count
    #     return self.count

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        row = len(grid)
        col = len(grid[0])

    # its is bfs problem explore at each level not possible do not go
        visited = set()
        queue = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        
        while queue:
            i , j = queue.popleft()
            directions = [(-1 ,0) , (1 , 0) , (0 , -1) , (0 , 1)]
            for nx , ny in directions:
                nx , ny = i+nx , j + ny
                if 0<= nx < row and 0 <= ny < col and grid[nx][ny] not in {0 , -1} and (nx , ny) not in visited:
                    grid[nx][ny] = grid[i][j] + 1
                    queue.append((nx , ny))
                    visited.add((nx , ny))

        