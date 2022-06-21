class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode, val: int) -> ListNode:
        temp, prev= head
        i = 1
        while (temp.next):
            if i % 2 == 0:
                curr = temp
                prev.next = temp.next
                prev = prev.next
            i = i + 1
            temp = temp.next
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