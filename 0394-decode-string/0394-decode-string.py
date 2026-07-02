class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        digits = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])

        for c in s:
            if c != ']':
                stack.append(c)
                continue

            contents = []
            number = []
            while stack[-1] != '[':
                contents.append(stack.pop())
            stack.pop()

            contents = ''.join(contents[::-1])

            while stack and stack[-1] in digits:
                number.append(stack.pop())
            
            number = int(''.join(number[::-1]))
            
            contents = contents * number

            stack.append(contents)
        
        return "".join(stack)



