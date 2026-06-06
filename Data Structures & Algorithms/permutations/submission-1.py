class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        def backtrack(lst_check , idx):
            if idx == len(nums):
                ans.append(lst_check)
                return

            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i) 
                    backtrack(lst_check + [nums[i]] , idx + 1)
                    visited.remove(i)
            
        
        backtrack([], 0)
    
        return ans
        