class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack) == 0:
            self.minStack.append(val)
            print('A ', self.minStack)
        elif val <= self.minStack[len(self.minStack) - 1]:
            self.minStack.append(val)
            print(self.minStack)

    def pop(self) -> None:
        val = self.stack.pop()
        
        if (val == self.minStack[len(self.minStack) - 1]):
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack) - 1]

    def minTop(self) -> int:
        pass
