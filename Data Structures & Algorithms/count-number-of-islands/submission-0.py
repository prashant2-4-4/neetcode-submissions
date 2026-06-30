from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        count = 0
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid[i][j] == '1':
                    # print((i,j))
                    count += 1
                    queue = deque()
                    queue.append((i,j))
                    visited.add((i,j))
                    while queue:
                        nx , ny = queue.popleft()

                        directions = [[-1 , 0] , [1,0] , [0 , -1] , [0 , 1]]

                        for dx , dy in directions:
                            n_nx = nx+ dx
                            n_ny = ny + dy
                            # print(n_nx , n_ny , grid[n_nx][n_ny] , visited)
                            if 0 <= n_nx < n and 0 <= n_ny < m and grid[n_nx][n_ny] == "1" and (n_nx , n_ny) not in visited:
                                # print('here' , (n_nx , n_ny))
                                queue.append((n_nx , n_ny))
                                visited.add((n_nx , n_ny))

        return count 




        