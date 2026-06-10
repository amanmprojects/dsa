class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0

        for operation in operations:
            match(operation):
                case "C":
                    popped = stack.pop()
                    result -= popped
                case "D":
                    if stack:
                        result += 2*stack[-1]
                        stack.append(2*stack[-1])
                case "+":
                    if stack:
                        result += stack[-1] + stack[-2]
                        stack.append(stack[-1]+ stack[-2])
                case _:
                    stack.append(int(operation))
                    result += int(operation)
            print(f"\"{operation}\"",stack, result)
        return result
        