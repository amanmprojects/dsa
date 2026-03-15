class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == '*':
                if not stack: 
                    stack.append('(')
                    continue
                if(stack[-1] == '('):
                    stack.pop()