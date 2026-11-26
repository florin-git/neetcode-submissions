class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # ))) (**
        # ((**)

        # ((*))

        # ((
            
        #     * 

        stack_parenthesis = []
        stack_asterisc = []

        for i, c in enumerate(s):
            if c == "(":
                stack_parenthesis.append(i)
            elif c == "*":
                stack_asterisc.append(i)
            else:
                if stack_parenthesis:
                    stack_parenthesis.pop()
                elif stack_asterisc:
                    stack_asterisc.pop()
                else:
                    return False

        while stack_parenthesis and stack_asterisc:
            if stack_asterisc.pop() < stack_parenthesis.pop():
                return False

        return len(stack_parenthesis) == 0





