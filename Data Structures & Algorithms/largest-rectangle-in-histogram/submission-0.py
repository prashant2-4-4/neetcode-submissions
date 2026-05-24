class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #monotonic increasing stack because smaller value we can not extent
        stack = []
        max_height = 0
        for i , h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx , he = stack.pop()
                max_height = max(max_height , (i - idx)*he)
                start = idx

            stack.append((start , h))

        #flush remainig

        for i , h in stack:
            max_height = max(max_height , (len(heights)-i)*h)

        return max_height        