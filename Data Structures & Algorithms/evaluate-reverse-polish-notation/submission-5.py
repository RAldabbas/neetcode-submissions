class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c.lstrip('-').isnumeric():
                stack.append(int(c))
                
            elif c == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif c == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif c == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif c == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))

        return stack.pop()
