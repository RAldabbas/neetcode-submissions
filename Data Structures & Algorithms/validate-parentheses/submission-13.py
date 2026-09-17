class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not len(s) or len(s) % 2 == 1:
            return False 
        for char in s:
            if char in ['[', '(', '{']:
                stack.append(char)
                continue
            if not stack:
                return False

            poppedEl = stack.pop()
            if char == '}' and poppedEl != '{':
                return False
            elif char == ')' and poppedEl != '(':
                return False
            elif char == ']' and poppedEl != '[':
                return False
        if stack:
            return False
        return True

        