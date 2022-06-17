# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.length = 0

class Solution:
    def hasCycle(self, head) -> bool:

        # if self.length < 2:
        #     return False
        
        # length = self.length

        # for i in range(0,length,2):
        #     pointer1 = self.head.next
        #     for j in range(1,length,1):
        #         pointer2= self.head
        #         if pointer1 == pointer2:
        #             return True
        #         pointer2 = pointer2.next
        #     pointer1 = pointer1.next


        # return False

        fast = head
        slow = head

        while (fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next

            if (fast == slow):
                return True

        
        return False

    def detectIndexCycle(self, head):
        fast = head
        slow = head
        while (fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next

            if (fast == slow):
                while head != slow:
                    head, slow = head.next, slow.next
                return head
    
        return None





