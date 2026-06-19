class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        if len(tokens) == 1:
            return int(tokens[0])

        for i in range(len(tokens)):
            try:
                stack.append(int(tokens[i]))
            except:
                if i < len(tokens) - 1:
                    stack.append(self.operation(tokens[i], stack.pop(), stack.pop()))
                else:
                    return self.operation(tokens[i], stack.pop(), stack.pop())

    def operation(self, op: str, b: int, a: int) -> int:
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return int(a / b)