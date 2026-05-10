class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        start,end = 0, len(heights) - 1

        while start < end:
            b = end - start
            if heights[start] < heights[end]:
                a = heights[start]
                start += 1
            else:
                a = heights[end]
                end -= 1   
            area = max(area, a * b) 

        return area

        