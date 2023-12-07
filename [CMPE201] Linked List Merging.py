#Create a new node
class Node:
    def __init__(self, data):
        self.data  = data
        self.next = None
#Create a new stack
class Stack:
    def __init__(self):
        self.top = None
    #Methods of the stack (peek, pop, push)
    def push(self, data):
        new_node=Node(data)
        if self.top:
            new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node=self.top
            self.top=self.top.next
            popped_node.next = None
            return popped_node.data
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
        
#Sample initialization
stack=Stack()
#Merging of two linked lists