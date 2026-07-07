class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def recursion(idx):
            if idx >= n:
                return 0

            if idx in memo:
                return memo[idx]
            
            rob = nums[idx] + recursion(idx+2)
            skip = recursion(idx+1)


            
            memo[idx]  = max(rob , skip)

            return memo[idx]

        return recursion(0)
        