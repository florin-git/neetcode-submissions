class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c not in par_map: # opening parenthesis
                stack.append(c)
                continue
            
            if not stack:
                return False
            # closing parenthesis
            p = stack.pop()
            if p != par_map[c]:
                return False
        
        return len(stack) == 0
                