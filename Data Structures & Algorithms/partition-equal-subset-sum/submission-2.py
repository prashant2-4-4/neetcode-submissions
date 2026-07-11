class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        n = len(nums)
        memo = {}
        def dfs(cum , idx):
            if (2 * cum) == total_sum:
                return True
            if idx == n:
                return False
            if (cum , idx) in memo:
                return memo[(cum,idx)]

            if dfs(cum + nums[idx] , idx+1):
                return True
            if dfs(cum , idx+1):
                return True
            
            memo[(cum,idx)] = False
            return memo[(cum,idx)]
        
        return dfs(0 , 0)