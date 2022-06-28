class MyCircularQueue :
    
    # private int[] data;
    # private int head;
    # private int tail;
    # private int size;

    # /** Initialize your data structure here. Set the size of the queue to be k. */
    
    def __init__(self, k: int):
        self.data = []
        self.head = -1
        self.tail = -1
        self.size = k

    
    # /** Insert an element into the circular queue. Return true if the operation is successful. */
    def enQueue(self,  value):
        if (self.isFull() == True):
            return False
        if (self.isEmpty() == True):
            self.head = 0

        self.tail = (self.tail + 1) % self.size
        self.data[self.tail] = value
        return True
    
    
    # /** Delete an element from the circular queue. Return true if the operation is successful. */
    def deQueue(self):
        if (self.isEmpty() == True): 
            return False
        if (self.head == self.tail):
            head = -1
            tail = -1
            return True
        self.head = (self.head + 1) % self.size;
        return True
    
    # /** Get the front item from the queue. */
    def Front(self):
        if (self.isEmpty() == True):
            return -1

        return self.data[self.head]
    
    # /** Get the last item from the queue. */
    def Rear(self):
        if (self.isEmpty() == True):
            return -1
        return self.data[self.tail]
    
    # /** Checks whether the circular queue is empty or not. */
    def isEmpty(self):
        return self.head == -1
    
    # /** Checks whether the circular queue is full or not. */
    def isFull(self):
        return ((self.tail + 1) % self.size) == self.head
    


# /**
#  * Your MyCircularQueue object will be instantiated and called as such:
#  * MyCircularQueue obj = new MyCircularQueue(k);
#  * boolean param_1 = obj.enQueue(value);
#  * boolean param_2 = obj.deQueue();
#  * int param_3 = obj.Front();
#  * int param_4 = obj.Rear();
#  * boolean param_5 = obj.isEmpty();
#  * boolean param_6 = obj.isFull();
#  */