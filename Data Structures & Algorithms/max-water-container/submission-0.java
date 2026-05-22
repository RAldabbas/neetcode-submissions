class Solution {
    public int maxArea(int[] heights) {
        int largestArea = 0;
        int left = 0;
        int right = heights.length - 1;
        
        while (left != right) {
            int currArea = Math.min(heights[left], heights[right]) * (right - left);
            largestArea = Math.max(largestArea, currArea);
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        return largestArea;
    }
}
