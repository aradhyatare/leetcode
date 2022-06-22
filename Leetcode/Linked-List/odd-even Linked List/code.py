class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode, val: int) -> ListNode:
        odd = head
        even = head.next
        evenHead = even
         
        while (even != None and even.next != None):
                odd.next = even.next
                odd = odd.next
                even.next = odd.next
                even = even.next
        odd.next = evenHead
        return head
            
        






#      print()


# 1->2->3->4->5
# While(temp.next)
#     temp = head #2 i = 1
#     prev = head #2
#     temp = temp.next #3 i = 2
#     if i %2 == 0:
#         prev.next = temp.next 1->3->2->4->5
#         prev = prev.next
#     i += 1


# 2->4->1->3->5