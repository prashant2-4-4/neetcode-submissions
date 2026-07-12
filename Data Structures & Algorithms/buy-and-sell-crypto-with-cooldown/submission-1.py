class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dfs(idx , buy):
            if idx >= n:
                return 0

            
            if (idx,buy) in memo:
                return memo[(idx , buy)]
            

            if buy:
                buy_pro = dfs(idx+1 , False) - prices[idx]
            
            else:
                sell_pro = dfs(idx+2 , True) + prices[idx]
            
            cool_down = dfs(idx+1 , buy)

            if buy:
                memo[(idx , buy)] =  max(buy_pro , cool_down)
            
            else:
                memo[(idx , buy)] =  max(sell_pro , cool_down)
            
            return memo[(idx , buy)]

        
        return dfs(0 , True)