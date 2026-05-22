class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        int longest = 0;
        for (int num : nums) {
            numSet.add(num);
        }

        for (int num : numSet) {
            if (!numSet.contains(num - 1)) {
                int tempLongest = 1;
                int currNum = num;

                while (numSet.contains(currNum + 1)) {
                    tempLongest++;
                    currNum++;
                }

                longest = Math.max(longest, tempLongest);
            }
        }
        return longest;
    }
}
