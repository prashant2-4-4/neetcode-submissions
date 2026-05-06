class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR cancels equal numbers: a ^ a = 0
        # (n * (n+1))/2 - sum(current one)
        res = len(nums) # because i ^ num for each index → this covers 0 to n-1 and all values in nums but not last value that's why
        for i , num in enumerate(nums):
            print(num)
            res ^= i ^ num
        return res
            

        