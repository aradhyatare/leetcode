# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        size = 1
        temp = head
        while (temp.next != None):
            temp = temp.next
            size += 1
        
        print(size)
        if (size==1):
            head = head.next
            return head
        
        if (size==n):
            head = head.next
            return head
        index = size - n 
        
        curr = head
        for _ in range(index):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        
        return head
            
        