# min heap + djikstra algo
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        row , col = len(grid) , len(grid[0])
        heap = []
        heapq.heappush(heap , (grid[0][0] , 0 , 0))
        visited.add((0 , 0))
        directions = [(-1 , 0) , (1, 0) , (0 , 1) , (0 , -1)]
        while heap:
            val , r , c = heapq.heappop(heap)
            if r == row-1 and c == col-1:
                return max(val , grid[-1][-1])
            for dx , dy in directions:
                nx = r + dx
                ny = c + dy

                if 0 <= nx < row and 0 <= ny < col and (nx , ny) not in visited:
                    heapq.heappush(heap , (max(val , grid[nx][ny]) , nx , ny))
                    visited.add((nx , ny))


        

        