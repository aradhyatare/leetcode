# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        answer_set = set()
        
        while (headA != None):
            answer_set.add(headA)
            headA = headA.next
            
        while (headB != None):
            if (headB in answer_set):
                return headB
            answer_set.add(headB)
            headB = headB.next
            
        return None
        
            
        