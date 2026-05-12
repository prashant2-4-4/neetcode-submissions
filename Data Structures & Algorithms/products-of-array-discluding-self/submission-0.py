class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #product of everything to left and product of everything to its right
        n = len(nums)
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]
        
        for i in range(1 , n):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        for i in range(n-2 , -1 , -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        
        result = []

        for i in range(n):
            result.append(prefix[i]*suffix[i])
        
        return result