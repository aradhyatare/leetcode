# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA = headA 
        while nodeA:
            nodeA.val = -nodeA.val 
            nodeA=nodeA.next 
        
        res = headB 
        while res:
            if res.val<0:
                break 
            res=res.next
        
        nodeA = headA 
        while nodeA:
            nodeA.val=abs(nodeA.val)
            nodeA=nodeA.next
        return res