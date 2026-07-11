class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        curr_max , curr_min = 1 , 1

        for n in nums:

            temp = curr_max * n
            curr_max = max(temp, curr_min * n , n)
            curr_min = min(temp , curr_min * n , n)

            res = max(curr_max , res)
            
        
        return res
        
        
            
            