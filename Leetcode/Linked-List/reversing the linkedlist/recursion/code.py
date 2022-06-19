class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head

        rest = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return rest

    def reverse(self, head: ListNode)-> ListNode:

        if head is None:
            return head

        if head.next is None:
            return head

        temp = self.reverse(head)
        head.next.next = head
        head.next = None

        return temp

    def reverseLinkedList(self, head:ListNode)-> ListNode:

        end = None
        while head:
            end, head.next, head = head, end, head.next
        return end
        