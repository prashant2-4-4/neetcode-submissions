class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(idx , lst):
            if sum(lst) > target or idx >= n:
                return 
            if sum(lst) == target:
                ans.append(lst.copy())
                return
            

            backtrack(idx , lst + [nums[idx]])
            backtrack(idx+1 , lst)
            
            return 
        
        backtrack(0 , [])

        return ans                 
            

        