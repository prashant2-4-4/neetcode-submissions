class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()
        def backtrack(idx , lst , curr_sum):
            if curr_sum == target:
                ans.append(lst.copy())
                return
            if curr_sum > target or idx >= n:
                return 
            for i in range(idx,n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                backtrack(i+1 , lst + [candidates[i]] , curr_sum + candidates[i])
                # backtrack(i+1 , lst)
            
            return 
        
        backtrack(0 , [] , 0)

        return ans 