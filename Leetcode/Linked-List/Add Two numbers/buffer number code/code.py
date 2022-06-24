class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        cur_ind = res
        cur_digit = 0
        buf_digit = 0
        while(l1 is not None or l2 is not None):
            if(l1 is None):
                cur_digit = l2.val + buf_digit
                l2 = l2.next
            elif(l2 is None):
                cur_digit = l1.val + buf_digit
                l1 = l1.next
            else:
                cur_digit = l1.val + l2.val + buf_digit
                l1 = l1.next
                l2 = l2.next
            if cur_digit>9:
                buf_digit = 1
                cur_digit -= 10
            else:
                buf_digit = 0
            # buf_digit = 1 if cur_digit > 9 else 0 
            # cur_digit = cur_digit % 10
            
            cur_ind.next = ListNode(cur_digit)
            cur_ind = cur_ind.next
            
        if buf_digit>0:
            cur_ind.next = ListNode(buf_digit)
        
        return res.next