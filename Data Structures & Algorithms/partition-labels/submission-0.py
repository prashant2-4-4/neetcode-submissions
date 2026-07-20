class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastidx = {}

        for i , c in enumerate(s):
            lastidx[c] = i
        
        res = []
        size , end = 0 , 0

        for i , c in enumerate(s):
            size += 1
            end = max(end , lastidx[c])

            if i == end:
                res.append(size)
                size = 0
        return res
        