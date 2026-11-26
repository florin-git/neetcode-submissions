class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []

        for c in s:
            if c in {'(', '[', '{'}:
                stack.append(c)
                continue
            
            if c == ")":
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop()

            elif c == "]":
                if not stack or stack[-1] != "[":
                    return False
                else:
                    stack.pop()

            elif c == "}":
                if not stack or stack[-1] != "{":
                    return False
                else:
                    stack.pop()

        # if at the end the stack is not empty return False
        return len(stack) == 0

        
        