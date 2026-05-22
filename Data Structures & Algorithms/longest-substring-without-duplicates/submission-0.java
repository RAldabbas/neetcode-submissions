class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> mySet = new HashSet<>();
        int longest = 0;
        int l = 0;
        
        for (int r = 0; r < s.length(); ++r) {
            while (mySet.contains(s.charAt(r))) {
                mySet.remove(s.charAt(l));
                l++;
            }
            mySet.add(s.charAt(r));
            longest = Math.max(longest, mySet.size());
        }
        

        return longest;
    }
}
