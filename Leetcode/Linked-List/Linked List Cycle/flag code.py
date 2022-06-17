class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.flag = 0

class Solution:
    def hasCycle(self, head) -> bool:

        while(head != None):

            if (head.flag == 1):
                return True

            head.flag == 1
            head = head.next
        
        return False
