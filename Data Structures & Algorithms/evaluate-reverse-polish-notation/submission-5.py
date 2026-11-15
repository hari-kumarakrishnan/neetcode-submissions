class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(tokens[i])
            else:
                second, first = stack.pop(), stack.pop()
                stack.append(self.calculate(first, second, tokens[i]))
        return int(stack[-1])
    def calculate(self, first, second, operator):
        first, second = int(first), int(second)
        if operator == "*":
            return first * second
        elif operator == "/":
            return int(first / second)
        elif operator == "+":
            return first + second
        else:
            return first - second