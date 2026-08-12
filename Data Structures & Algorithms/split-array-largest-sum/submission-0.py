#it is good binary search problem , see solution and try to make sense , definetly backtracking is right solution that you thought intially.

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        lo , hi = max(nums) , sum(nums)

        def search(mid):
            step = 0
            curr_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > mid:
                    step += 1
                    curr_sum = num
            
            return step+1

        while lo <= hi:
            mid = (lo+hi)//2

            if search(mid) > k:
                lo = mid+1
            else:
                hi = mid - 1
        
        return lo
        