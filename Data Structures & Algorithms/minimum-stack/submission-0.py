class MinStack:

    def __init__(self):
        self.stack = []
        self.minima = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.minima or val <= self.minima[-1]:
            self.minima.append(val)
        

    def pop(self) -> None:

        val = self.stack.pop()
        if val == self.minima[-1]:
            self.minima.pop()

        # check if element I'm popping is the top in min
        # if yes pop also in min
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minima[-1]




        
