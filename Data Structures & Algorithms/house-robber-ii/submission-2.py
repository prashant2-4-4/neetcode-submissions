class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0] , nums[1])

        dp_1 = [0] * (n-1)

        dp_1[0] = nums[0]
        dp_1[1] = max(nums[0] , nums[1])

        for i in range(2 , n-1):
            dp_1[i] = max(dp_1[i-1] , dp_1[i-2] + nums[i])

        dp_2 = [0] * (n-1)
        dp_2[0] = nums[1]
        dp_2[1] = max(nums[2] , nums[1])

        for i in range(3 , n):
            dp_2[i-1] = max(dp_2[i-2] , dp_2[i-3] + nums[i])

        print(dp_1 , dp_2)
        return max(dp_2[-1] , dp_1[-1])
        