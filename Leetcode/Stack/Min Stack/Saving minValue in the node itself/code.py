class MinStack:

    def __init__(self):
        self.Stack = []
  
        

    def push(self, val: int) -> None:
        if self.Stack:
            minVal = min(val, self.Stack[-1][1])
        else:
            minVal = val
        self.Stack.append((val, minVal))
        
        

    def pop(self) -> None:
        self.Stack.pop()
        

    def top(self) -> int:
        return self.Stack[-1][0]
        
    def getMin(self) -> int:
        # listd = sorted(self.Stack)
        return self.Stack[-1][1]


obj = MinStack()
obj.push(2)
obj.push(3)
# print(obj.pop())
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)