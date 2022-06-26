class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None
        
        prehead = Node(0, head, None)
        while head:
            head.next = Node(head.val, head.next, None)
            head = head.next.next
            
        head = prehead.next
        while head:
            if head.random:
                head.next.random = head.random.next
            else:
                head.next.random = None
            head = head.next.next
            
        head = prehead.next
        new_head = head.next
        while head:
            next = head.next
            head.next = head.next.next
            if head.next:
                next.next = head.next.next
            else:
                next.next = None
            head = head.next
            
        return new_head