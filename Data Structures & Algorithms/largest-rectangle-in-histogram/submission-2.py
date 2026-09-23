class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                leftBound = stack[-1] if stack else -1
                rightBound = i
                width = rightBound - leftBound - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)

        return maxArea