import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        result = []

        for i in range(len(nums)):
            #remove indices outside window
            while dq and dq[0] < i-k+1:
                dq.popleft()

            #remove smaller element form back    
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)

            if i >= k-1:
                result.append(nums[dq[0]])
        return result



        