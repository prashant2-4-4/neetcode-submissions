class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nu = nums[0]

        for n in nums[1:]:
            nu = nu ^ n
        
        return nu
        