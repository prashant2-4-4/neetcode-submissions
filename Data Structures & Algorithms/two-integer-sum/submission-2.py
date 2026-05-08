from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # num_counter = Counter(nums)
        num_counter = {}

        for i , num in enumerate(nums):
            val = target - num

            if val in num_counter:
                return [num_counter[val] , i]
            
            num_counter[num] = i
        




        # nums.sort()
        # i = 0
        # j = len(nums) - 1
        # while(i < j):
        #     if nums[i] + nums[j] == target:
        #         return [i , j]
            
        #     if nums[i] + nums[j] > target:
        #         j -= 1

        #     if nums[i] + nums[j] < target:
        #         i += 1

        # return [-1 , -1] 