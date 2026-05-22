class Solution {
    public boolean isPalindrome(String s) {
        // char[] allChars = s.replace(" ", "").toLowerCase().toCharArray();
        String tempStr = s.replace(" ", "").toLowerCase();
        StringBuilder cleanedStr = new StringBuilder();
        for (char c : tempStr.toCharArray()) {
            if (Character.isLetter(c) || Character.isDigit(c)) {
                cleanedStr.append(c);
            }
        }

        return cleanedStr.toString().equals(cleanedStr.reverse().toString());
        
    }
}
