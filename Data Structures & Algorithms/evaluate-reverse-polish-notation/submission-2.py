class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stack.append(int(t))
                continue
            
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                num = a + b
            elif t == "-":
                num = a - b
            elif t == "*":
                num = a * b
            elif t == "/":
                # num = a // b
                num = int(float(a) / b)
            stack.append(num)

        return stack[-1]
        