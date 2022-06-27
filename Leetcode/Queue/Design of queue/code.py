from collections import deque
# import queue


class MyCircularQueue:

    queue = deque()
    loq = 0
    def __init__(self, k: int):
        # q = Queue(maxsize = k)
        # print("A")
        self.length = k
        

    def enQueue(self, value: int) -> bool:
        if self.loq<self.length:
            self.queue.append(value)
            self.loq += 1
            return True
        return False
        
    def deQueue(self) -> bool:
        if self.loq != 0:
            if (self.queue.popleft()):
                self.loq -= 1
                return True
        return False

    def Front(self) -> int:
        if self.loq == 0:
            return -1
        return self.queue[0]

    def Rear(self) -> int:
        if self.loq == 0:
            return -1
        return self.queue[-1]
        
    def isEmpty(self) -> bool:
        if self.loq == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.loq == self.length:
            return True
        return False

    def print(self):
        print(self.queue)
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(2)
# param_1 = obj.enQueue(2)
# param_1 = obj.enQueue(3)
# print(obj.enQueue(4))

print(obj.Rear())
print(obj.Front())
# param_2 = obj.deQueue()
# obj.print()

# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()