class MinStack:

    def __init__(self):
        self.Stack = []
        
    def push(self, val: int) -> None:
        self.Stack.append(val)

    def pop(self) -> None:
        # var = self.Stack[-1]
        self.Stack.pop()
        # print(f"Deleting {var}")
        return 

    def top(self) -> int:
        return self.Stack[-1]
        
    def getMin(self) -> int:
        listd = sorted(self.Stack)
        return listd[0]