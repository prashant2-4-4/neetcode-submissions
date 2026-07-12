class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def dfs(idx , sub_amount):

            if sub_amount == amount:
                return 1
            if sub_amount > amount:
                return 0
            if idx == n:
                return 0
            
            if (idx,sub_amount) in memo:
                return memo[(idx,sub_amount)]
            
        
            move = dfs(idx+1 , sub_amount)
            
                
            take = dfs(idx , sub_amount + coins[idx] )
            memo[(idx,sub_amount)] = move + take
            return memo[(idx,sub_amount)]
         

        

        return dfs(0 , 0)

        