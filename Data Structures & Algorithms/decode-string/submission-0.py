class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
                continue

            res = []
            while stack[-1] != "[":
                res.append(stack.pop())
            stack.pop()

            num = 0
            j = 0
            while stack and stack[-1].isdigit():
                num += int(stack.pop()) * (10 ** j)
                j += 1

            stack.append(num * "".join(res[::-1]))

        return "".join(stack)
        
