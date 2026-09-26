class MinStack:
    def __init__(self):
        self.stack=[]
        self.mstack=[]
    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.mstack or value<=self.mstack[-1]:
            self.mstack.append(value)
        else:
            self.mstack.append(self.mstack[-1])
    def pop(self) -> None:
        self.stack.pop()
        self.mstack.pop() 
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.mstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()