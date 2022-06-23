class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number1 = ''
        number2 = ''
        head = None
        head1 = l1
        head2 = l2

        while(head1 != None):
            number1 += str(head1.val)
            head1 = head1.next
        
        while(head2 != None):
            number2 += str(head2.val)
            head2 = head2.next
        number1 = number1[::-1]
        number2 = number2[::-1]
        sum_list = int(number1) + int(number2)
        # print(number1)
        # print(number2)
        # print(sum_list)
        # numbers = (str(sum_list)).split()
        numbers = [int(a) for a in str(sum_list)]
        # numbers = numbers[::-1]   
        # print(numbers)
        for i in range(len(numbers)):
            new_node = ListNode(numbers[i])
            # head = new_node
            new_node.next = head
            head = new_node
            
        return head 
        