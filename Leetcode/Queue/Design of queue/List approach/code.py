class MyCircularQueue:
    def __init__(self, k: int):
        self.data = []
        self.maxSize = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data.append(value)
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.data.pop(0)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return - 1
        return self.data[0]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[-1]

    def isEmpty(self) -> bool:
        return self.data == []

    def isFull(self) -> bool:
        return len(self.data) == self.maxSize