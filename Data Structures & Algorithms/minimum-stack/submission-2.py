class MinStack:

    def __init__(self):
        self.stack = []
        self.minima = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        minimum = self.minima[-1] if self.minima else float("inf")
        if val < minimum:
            self.minima.append(val)
        else:
            self.minima.append(minimum)


    def pop(self) -> None:
        self.stack.pop()
        self.minima.pop()
        

    def top(self) -> int:
        # self.minima.pop()
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minima[-1]
        
# mins:  1 1 0 0
# stack: 1 2 0 5