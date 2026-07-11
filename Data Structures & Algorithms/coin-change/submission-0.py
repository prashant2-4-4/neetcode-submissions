class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {}
        def dfs(val):
            if val == amount:
                return 0

            if val > amount:
                return float('inf')
            
            if val in dp:
                return dp[val]

            best = float('inf')
            for coin in coins:
                res = dfs(val+coin)
                
                if res != float('inf'):
                    best = min(res+1 , best)
            dp[val] = best
            
            return dp[val]
            # for coin in coins:
            #     if dfs(val + coin , depth + 1):
            #         dp[val+coin] = depth + 1
            #         return dp[val+coin]
            #     else:
            #         dp[val+coin] = 0
            
        ans =  dfs(0 )
        return -1 if ans == float("inf") else ans


            

                

        