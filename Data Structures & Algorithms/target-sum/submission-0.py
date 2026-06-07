class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtrack(idx , su):
            if idx == len(nums):
                return 1 if su == target else 0
            if (idx ,  su) in memo:
                return memo[(idx , su)]
            memo[(idx , su)] = (backtrack(idx+1 , su + nums[idx]) +
             backtrack(idx+1 , su - nums[idx]))
            
            return memo[(idx , su)]
        
        return backtrack( 0 ,0)
            

                


        