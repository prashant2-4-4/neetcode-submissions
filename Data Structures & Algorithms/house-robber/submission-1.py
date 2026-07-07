# recursion , memo and then dp
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # memo = {}
        # def recursion(idx):
        #     if idx >= n:
        #         return 0

        #     if idx in memo:
        #         return memo[idx]
            
        #     rob = nums[idx] + recursion(idx+2)
        #     skip = recursion(idx+1)


            
        #     memo[idx]  = max(rob , skip)

        #     return memo[idx]

        # return recursion(0)

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0] , nums[1])

        for i in range(2 , n):
            dp[i] = max(dp[i-1] , dp[i-2] + nums[i])
        
        return dp[-1]
        