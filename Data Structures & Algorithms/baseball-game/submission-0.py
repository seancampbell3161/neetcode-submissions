class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                stack.append(int(stack[-2]) + int(stack[-1]))
                continue
            if op == 'D':
                stack.append(int(stack[-1]) * 2)
                continue
            if op == 'C':
                stack.pop()
                continue
            stack.append(int(op))
        return sum(stack)