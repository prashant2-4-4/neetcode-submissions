
class Solution:
    def __init__(self, w: List[int]):
        if w:
            self.prefix_sum = [w[0]]
            for we in w[1:]:
                last_prefix = self.prefix_sum[-1]
                self.prefix_sum.append(we + last_prefix)
        

    def pickIndex(self) -> int:
    
        number = random.randint(1 ,self.prefix_sum[-1])

        lo , hi = 0 , len(self.prefix_sum)-1
        while lo < hi:
            mid = (lo+hi)//2

            if self.prefix_sum[mid] < number:
                lo = mid + 1
            else:
                hi = mid
        
        return lo
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()