class MinStack:

    def __init__(self):
        self.stack = [(float("inf") , float("inf"))]
        

    def push(self, val: int) -> None:
        if val < self.stack[-1][1]:
            self.stack.append((val , val))
        else:
            self.stack.append((val , self.stack[-1][1]))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
        
