class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        def backtrack(idx , subset):
            if idx == len(nums):
                out.append(subset[:])
                return
            
            #include

            subset.append(nums[idx])
            backtrack(idx +1 , subset)
            subset.pop()

            #donot include

            while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            
            backtrack(idx+1 , subset)
        
        backtrack(0 , [])
        return out