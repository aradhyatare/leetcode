from asyncio.windows_events import NULL
from re import L


class MyLinkedList:

    def __init__(self):
        "Initialise the data strucutre"
        self.head = None
        self.length = 0
        

    def get(self, index: int) -> int:
        "Get the value of the indexth node in the linked list. If the index is invalid, return -1"
        if index > self.length:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr['next']
        return curr['val']
        

    def addAtHead(self, val: int) -> None:
        "Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list."
        # curr = self.head
        new_node = {}
        new_node['val'] = val
        new_node['next'] = self.head
        self.head = new_node
        self.length += 1

        

    def addAtTail(self, val: int) -> None:
        "Append a node of value val as the last element of the linked list"

        new_node = {}
        new_node['val'] = val 
        new_node['next'] = None
        prev = self.head
        for i in range(self.length-1):
            prev = prev['next']
        prev['next'] = new_node
        self.length += 1

        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the indexth node in the linked list. 
        If index equals the length of the linked list, the node will be appended to the end of the linked list.
        If index is greater than the length, the node will not be inserted.
        """

        if index > self.length:
            return 

        if index == self.length:
            MyLinkedList.addAtTail(val)
            return
        
        new_node = {}
        new_node['val'] = val
        prev = self.head
        for i in range(index):
            prev = prev['next']
        new_node['next'] = prev['next']
        prev['next'] = new_node
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        "Delete the indexth node in the linked list, if the index is valid"
        
        if index >= self.length:
            return

        if index == 0:
            self.head = self.head['next']
            return

        curr = self.head
        for i in range(index):
            prev = curr
            curr = curr['next']

        prev['next'] = curr['next']

        self.length -= 1
    
    def printlist(self):
        curr= self.head
        for i in range(self.length):
            print(curr['val'])
        
        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(1)
obj.addAtHead(1)
print(f"Printing list before deleting it {obj.printlist()}", end=" ")
obj.addAtTail(3)
print(f"Printing list before deleting it {obj.printlist()}", end=" ")
obj.addAtIndex(1,2)
# print(obj.get(1))
print(f"Printing list before deleting it {obj.printlist()}", end=" ")
obj.deleteAtIndex(1)
# print(obj.get(1))
print(f"Printing list after deleting it {obj.printlist()}", end=" ")