class Solution {
    public boolean isValid(String s) {
        Stack<Character> charStack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                charStack.push(c);
            } else if (charStack.isEmpty()) {return false;}

            if (c == ')' && !charStack.isEmpty() && charStack.pop() != '(') {
                return false;
            } 
            else if (c == '}' && !charStack.isEmpty() && charStack.pop() != '{') {
                return false;
            }
            else if (c == ']' && !charStack.isEmpty() && charStack.pop() != '[') {
                return false;
            }
        }
        return charStack.isEmpty();
    }
}
