class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() #nlogn
        res = []
        print(nums)
        for i , val in enumerate(nums):

            start, end = i+1, len(nums) - 1
            target = -val
            # to skip dupliactes
            if i> 0  and nums[i] == nums[i-1]:
                continue
            while start < end:
                curr_sum = nums[start] + nums[end]
                if curr_sum == target:
                    res.append([val , nums[start] , nums[end]])
                    start += 1
                    #duplicate removal
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                elif curr_sum < target:
                    start += 1
                else:
                    end -= 1

        return res
        