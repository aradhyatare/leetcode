

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self):
        "Initialise the data strucutre"
        self.head = None
        self.length = 0


    def removeElements(self, head: ListNode, val: int):
        curr = head
        if (curr == None):
            return
        i = 0
        while (curr.next):
            prev = curr
            curr = curr.next

            if (curr.val == val):
                i += 1
                print(curr.val)
                prev.next = curr.next
           
        return head

    
    def addAtHead(self, val: int) -> None:
        "Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list."
        # curr = self.head
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def printlist(self):
        curr= self.head
        for i in range(self.length):
            print(curr.val)
            curr = curr.next

    def getLinkedList(self):
        return self.head

    def remove(self, val):
        LinkedList = self.removeElements(self.getLinkedList(),val)
        curr = LinkedList.head
        while(curr):
            print(curr.val)
            curr = curr.next
        

obj = Solution()
obj.addAtHead(1)
obj.addAtHead(2)
obj.addAtHead(3)
obj.addAtHead(4)
obj.addAtHead(5)
obj.addAtHead(6)
obj.addAtHead(6)
obj.printlist()
linkedList = obj.getLinkedList()
print(linkedList)
val = obj.remove(1)
print(val)
