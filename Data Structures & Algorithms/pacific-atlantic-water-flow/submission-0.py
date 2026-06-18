#approach of finding intersactions
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row , col = len(heights) , len(heights[0])
        pac , atl = set() , set()
        def dfs(r , c , visit , prevHeight):
            if ((r,c) in visit or 
                r < 0 or r == row or c < 0 or c==col 
                or heights[r][c] < prevHeight):

                return 
            
            visit.add((r,c))
            curr_height = heights[r][c]
            #traserve in every direction
            dfs(r+1 , c, visit , curr_height)
            dfs(r-1 , c, visit , curr_height)
            dfs(r , c+1, visit , curr_height)
            dfs(r , c-1, visit , curr_height)

        
        for r in range(row):
            dfs(r , 0 , pac , heights[r][0]) # pacific ocean
            dfs(r , col-1 , atl , heights[r][col-1]) # altanic ocean
        
        for c in range(col):
            dfs(0 , c , pac , heights[0][c])
            dfs(row-1 , c , atl , heights[row-1][c])
        
        res = []

        for r in range(row):
            for c in range(col):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
                


        return res
        
