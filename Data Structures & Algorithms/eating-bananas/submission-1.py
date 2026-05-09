class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        start , end = 1 , max(piles)
        while(start < end):
            mid = (start+end)//2
            hours= 0
            for pile in piles:
                # hours += (pile//mid)
                # if pile%mid:
                #     hours += 1
                hours += math.ceil(pile/mid)
            

            if hours <= h:
                end = mid
            else:
                start = mid+1

        return start
        

