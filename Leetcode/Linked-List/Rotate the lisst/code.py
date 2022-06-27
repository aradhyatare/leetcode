class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self):
        "Initialise the data strucutre"
        self.head = None

    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None: return head
        if head.next == None: return head
        if k == 0: return head
        curr = head
        length = 1
        while curr.next != None:
            if curr.next != None:
                prev = curr
                curr = curr.next
                length += 1 
        # print(length)
        # k = (str(k)).strip('0')
        # k = int(k)
        # print(k)
        if k>=2*length:
            # print(k)
            k = k % length
            # print(k)
            
        while k!= 0:
            while curr.next != None:
                if curr.next != None:
                    prev = curr
                    curr = curr.next
            # print(f"Current Value is {curr.val}")
            # print(f"Previous Value is {prev.val}")
            if curr.next == None:
                prev.next = None
                last = curr
                last.next = head
                head = last
            # print(f"Current Value is {curr.val}")
            # print(f"Previous Value is {prev.val}")
            k -= 1
        return head

    def addAtHead(self, val: int) -> None:
        "Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list."
        # curr = self.head
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        curr= self.head
        while curr:
            print(curr.val, end=',')
            curr = curr.next
        
        self.rotateRight(self.head,1)

# [1,2,3]
# 2000000000
1 - 3, 1, 2
2 - 2, 3, 1
3 - 1, 2, 3 
        

myobj = Solution()
myobj.addAtHead(5)
myobj.addAtHead(4)
myobj.addAtHead(3)
myobj.addAtHead(2)
myobj.addAtHead(1)
myobj.printlist()
# myobj.rotateRight()
# myobj.printlist()