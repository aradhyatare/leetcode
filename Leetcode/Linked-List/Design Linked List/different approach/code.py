class ListNode:
    def __init__(self,x):
        self.val=x
        self.next= None
        
class MyLinkedList:
    def __init__(self):
        self.size=0
        self.thead=ListNode(0)

    def get(self, index: int) -> int:
        if index<0 or self.size<=index:
            return -1
        curr=self.thead
        for _ in range(index+1):
            curr=curr.next
        return curr.val
            
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return
        if index<0:
            index=0
        self.size+=1
        curr=self.thead
        for _ in range(index): 
            curr=curr.next
            
        nnode=ListNode(val)
        nnode.next=curr.next
        curr.next=nnode
        
            
    def deleteAtIndex(self, index: int) -> None:
        if index>=self.size or index<0:
            return 
        curr=self.thead
        for i in range(index):
            curr=curr.next
        
        curr.next=curr.next.next
        self.size-=1
