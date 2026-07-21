class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row , col = len(obstacleGrid) , len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1
        for r in range(1 , row):
            if obstacleGrid[r][0] == 0: 
                dp[r][0] = dp[r-1][0]
        
        for c in range(1 , col):
            if obstacleGrid[0][c] == 0: 
                dp[0][c] = dp[0][c-1]
            

        for r in range(1 , row):
            for c in range(1 , col):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = max(dp[r][c] , dp[r][c-1] + dp[r-1][c])

        return dp[-1][-1] 