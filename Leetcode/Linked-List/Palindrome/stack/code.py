# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = head
        stack = []
        ispalin = True
        while(temp != None):
            stack.append(temp.val)
            
            temp = temp.next
            
        while (head != None):
            i = stack.pop()
            
            if (i == head.val):
                ispalin = True
            else:
                ispalin = False
                break
            head = head.next
                
        return ispalin