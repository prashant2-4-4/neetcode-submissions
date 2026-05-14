class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start ,end = 0 , len(heights)-1
        score = 0

        while(start < end):
            curr_score = (end-start) * min(heights[start] ,heights[end])
            score = max(score , curr_score)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return score

        