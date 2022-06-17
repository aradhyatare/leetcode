# Definition for singly-linked list.

# If you want to see the index at which the linkedlist is cyclic then instead of returning True or false return head and none

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.length = 0

class Solution:
    def hasCycle(self, head) -> bool:
        head_set = set()
        while(head != None):
            if head in head_set:
                return True
            head_set.add(head)
            head = head.next
        return False