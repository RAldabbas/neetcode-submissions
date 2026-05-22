class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answers = new int[nums.length];
        int total = 1;
        int numZeroes = 0;
        for (int num : nums) {
            if (num != 0) {
               total *= num; 
            } else {
                numZeroes++;
            }
        }

        if (numZeroes > 1) {
            return answers;
        }

        for (int i = 0; i < nums.length; ++i) {
            if (numZeroes == 0) {
                answers[i] = total / nums[i];
            } else {
                if (nums[i] == 0) {
                    answers[i] = total;
                } else {
                    answers[i] = 0;
                }
            }
        }
        return answers;
    }
}  
