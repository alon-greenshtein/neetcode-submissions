class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        for i in range(len(heights)):
            for j in range(1, len(heights)):
                a = min(heights[i],heights[j])
                b = j - i
                area = max(area, a * b)
        return area

        