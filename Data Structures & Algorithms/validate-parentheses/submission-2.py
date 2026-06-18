class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {'(': ')', '[': ']', '{': '}'}

        for p in s:
            if p in map:
                stack.append(p)
            elif len(stack) == 0 or map[stack.pop()] != p:
                return False

        return len(stack) == 0
