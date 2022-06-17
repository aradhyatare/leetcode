class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.length = 0

class Solution:
    def hasCycle(self, head) -> bool:

        temp = ''
        while (head != None and head.next != None):

            if (head.next == temp):
                return True

            next = head.next

            head.next = temp

            head = next
        
        return False

