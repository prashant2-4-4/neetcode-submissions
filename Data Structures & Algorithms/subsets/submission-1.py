class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        def backtrack(lst , idx):
            if idx == len(nums):
                output.append(lst[:])
                return
            

            backtrack(lst , idx + 1)
            lst.append(nums[idx])
            backtrack(lst  , idx + 1)
            lst.pop()
        
        backtrack([] , 0)
        return output
        