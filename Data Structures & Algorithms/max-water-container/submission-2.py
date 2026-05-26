class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        largest = 0
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            largest = max(area, largest)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return largest


