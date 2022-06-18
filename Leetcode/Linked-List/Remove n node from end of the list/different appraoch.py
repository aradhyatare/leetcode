class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        ahead = head
        
        for i in range(n):
            ahead = ahead.next
            
        if not ahead:
            return head.next
        
        while ahead.next:
            curr = curr.next
            ahead = ahead.next
        
        curr.next = curr.next.next
        
        return head