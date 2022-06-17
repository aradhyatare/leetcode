class Node:

    def __init__(self, val= None, next_node = None):
        self.val = val
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        "Initialise the data strucutre"
        self.head = None
        self.length = 0
        

    def get(self, index: int) -> int:
        "Get the value of the indexth node in the linked list. If the index is invalid, return -1"
        if index >= self.length:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next 
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        "Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list."
        # curr = self.head
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

        

    def addAtTail(self, val: int) -> None:
        "Append a node of value val as the last element of the linked list"

        if self.length == 0:
            self.addAtHead(val)
            return

        new_node = Node(val)
        new_node.next = None
        prev = self.head
        for i in range(self.length-1):
            prev = prev.next
        prev.next = new_node
        self.length += 1

        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the indexth node in the linked list. 
        If index equals the length of the linked list, the node will be appended to the end of the linked list.
        If index is greater than the length, the node will not be inserted.
        """

        if index > self.length:
            return 
        # print(f"index:{index} and value = {val}")
        # if index == self.length:
        #     self.addAtTail(val)
        #     return
        if index == 0:
            self.addAtHead(val)
            return
        
        new_node = Node(val)
        prev = self.head
        for i in range(index-1):
            prev = prev.next
        new_node.next = prev.next
        prev.next = new_node
       
        

    def deleteAtIndex(self, index: int) -> None:
        "Delete the indexth node in the linked list, if the index is valid"
        
        if index >= self.length:
            return

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        curr = self.head
        for i in range(index):
            prev = curr
            curr = curr.next

        prev.next = curr.next

        self.length -= 1
    
    def printlist(self):
        curr= self.head
        for i in range(self.length):
            print(curr.val, end=',')
            curr = curr.next


List1 = ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get","get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"]
List2 = [[],[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]]
# obj = MyLinkedList()
for i in range(1,len(List1)):
    operations = List1[i]
    values = '(' + str(List2[i][0]) + ')'
    statement = 'obj.' + operations + values
    print(statement)
    print("obj.printlist()")
    # print(f"The operation is {statement} and the value is {obj.printlist()}")
    # obj.statement
    # print(f"The operation is {statement} and the value is {obj.printlist()}")

        
# 
# ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
# [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
        
# ["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
# [[],[0,10],[0,20],[1,30],[0]]
# 

# ["MyLinkedList","addAtTail","get"]
# [[],[1],[0]]

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(1)
obj.addAtHead(1)
obj.printlist()
obj.addAtTail(3)
obj.printlist()
obj.addAtIndex(1,2)
obj.printlist()
obj.get(1)
obj.printlist()
obj.deleteAtIndex(1)
obj.printlist()
obj.get(1)
obj.printlist()
obj.get(3)
obj.printlist()
obj.deleteAtIndex(3)
obj.printlist()
obj.deleteAtIndex(0)
# obj.printlist()
obj.get(0)
# obj.printlist()
obj.deleteAtIndex(0)
# obj.printlist()
obj.get(0)
# obj.printlist()
# obj.addAtHead(4)
# obj.printlist()
# obj.get(1)
# obj.printlist()
# obj.addAtHead(1)
# obj.printlist()
# obj.addAtHead(5)
# obj.printlist()
# obj.deleteAtIndex(3)
# obj.printlist()
# obj.addAtHead(7)
# obj.printlist()
# obj.get(3)
# obj.printlist()
# obj.get(3)
# obj.printlist()
# obj.get(3)
# obj.printlist()
# obj.addAtHead(1)
# obj.printlist()
# obj.deleteAtIndex(4)
# obj.printlist()
# obj.addAtTail
# obj.addAtIndex(0,10)
# obj.addAtIndex(0,20)
# obj.addAtIndex(1,30)
# obj.printlist()
# print(obj.get(0))
# obj.addAtHead(7)
# obj.addAtHead(2)
# obj.addAtHead(1)
# obj.addAtIndex(3,0)
# obj.printlist()
# obj.deleteAtIndex(2)
# obj.printlist()
# obj.addAtHead(6)
# obj.addAtTail(4)
# obj.printlist()
# obj.get(4)
# obj.addAtHead(4)
# obj.addAtIndex(5,0)
# obj.addAtHead(5)

# print(f"Printing list before deleting it {obj.printlist()}", end=" ")
# obj.addAtTail(3)
# # obj.printlist()
# # print(f"Printing list before deleting it {obj.printlist()}", end=" ")
# obj.addAtIndex(1,2)
# obj.printlist()
# print(obj.get(1))
# # print(f"Printing list before deleting it {obj.printlist()}", end=" ")
# obj.deleteAtIndex(1)
# print(obj.get(1))
# # print(f"Printing list after deleting it {obj.printlist()}", end=" ")