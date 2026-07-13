class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        jump = 0
        n = len(nums)
        curr_end = 0
        for i in range(n-1):
            farthest = max(farthest , i + nums[i])

            if i == curr_end:
                jump += 1
                curr_end = farthest

        
        return jump