class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        int longest = 1;
        if (nums.length == 0) {
            return 0;
        }
        for (int num : nums) {
            numSet.add(num);
        }

        for (int num : nums) {
            int tempLongest = 1;
            int currNum = num;
            while (true) {
                if (numSet.contains(currNum + 1)) {
                    tempLongest += 1;
                    currNum += 1;
                } else {
                    break;
                }
            }
            if (tempLongest > longest) {
                longest = tempLongest;
            }
        }
        return longest;
    }
}
