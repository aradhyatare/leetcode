class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Node:
        if not head: return head
        dummy = Node(0)
        cur, stack = dummy, [head]
        while stack:
            tmp = stack.pop()
            if tmp.next: stack.append(tmp.next)
            if tmp.child: stack.append(tmp.child)
            cur.next = tmp
            tmp.prev = cur
            tmp.child = None
            cur = tmp
        dummy.next.prev = None
        return dummy.next
    

    # def headchild(self, child: Node) -> Node:
        
    #     curr = child.head
    #     while (curr != None):
    #         if (curr.child == None):
    #             curr = curr.next
    #         if (curr.child != None):
    #             temp = curr.next
    #             while (curr.child
    #             curr.next = curr.child.next

