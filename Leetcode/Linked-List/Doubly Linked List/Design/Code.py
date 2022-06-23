import gc


class Node:
    def __init__(self, next = None, prev = None, data = None):
        self.next = next
        self.prev = prev
        self.data = data
   
class LinkedList:

    def __init__(self):
        "Initialise the data strucutre"
        self.head = None
        self.length = 0

    def push(self, new_data):

        new_node = Node(data=new_data)

        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insertAfter(self, prev_node, new_data):

        new_node = Node(data=new_data)

        if prev_node is None:
            print("Node is not present in the DLL")
            return
        
        new_node.next = prev_node.next #Chaning the new_node's next to prev node's next.
        prev_node.next = new_node #Changing the next of prev node to new_node

        new_node.prev = prev_node #Changing the prev of new_node to previous.

        if new_node.next is not None: #Now if new_node.next is not then we'll change new_node.next's prev to new_node
            new_node.next.prev = new_node

    
    def append(self,new_data):

        new_node = Node(data=new_data)
        new_node.next = None

        temp = self.head

        if (self.head is None):
            new_node.prev = None
            self.head = new_node
            return

        while(temp.next is not None):
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp

    def insertBefore(self, next_node, new_data):

        new_node = Node(data=new_data)

        if next_node is None:
            print("Node is not present in the DDL")
            return

        new_node.prev = next_node.prev
        next_node.prev = new_node
        new_node.next = next_node

        if new_node.prev is not None:
            new_node.prev.next = new_node
        else:
            self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(" {}".format(temp.data))
            temp = temp.next

    def deleteNode(self, dele):

        if self.head is None or dele is None:
            return

        if self.head == dele:
            self.head = dele.next

        if dele.next is not None:
            dele.next.prev = dele.prev

        if dele.prev is not None:
            dele.prev.next = dele.next

        gc.collect()

    def remove(self):
        if self.head is None:
            return
        
        if self.head.next is not None:
            self.head = self.head.next
            self.head.prev = None

    def pop(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while(temp.next.next != None):
                    temp = temp.next
                # lastNode = temp.next
                temp.next = None
                # lastNode = None

Myobject = LinkedList()
Myobject.append(1)
Myobject.append(3)
Myobject.append(2)
Myobject.append(5)
Myobject.append(7)
Myobject.append(6)
Myobject.insertAfter(Myobject.head.next,11)
Myobject.insertBefore(Myobject.head,20)
Myobject.printList()
print("deleting the node")
Myobject.deleteNode(Myobject.head.next.next.next.next.next.next.next)
Myobject.printList()
print("Removing the first node")
Myobject.remove()
Myobject.printList()
print("Removing the Last node")
Myobject.pop()
Myobject.printList()

         
        

       


        
