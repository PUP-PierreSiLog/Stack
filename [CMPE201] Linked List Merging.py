#Create a new node
class Node:
    def __init__(self, data):
        self.data  = data
        self.next = None

#Links the created lists
def link_linked_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    current = list1
    while current.next:
        current = current.next
    current.next = list2
    return list1

def merge(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next

#Sorts the created lists
def merge_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    mid = find_middle(head)
    second_half = mid.next
    mid.next = None

    sorted_first_half = merge_sort_linked_list(head)
    sorted_second_half = merge_sort_linked_list(second_half)

    return merge(sorted_first_half, sorted_second_half)

def find_middle(head):
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

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
        
list1 = Node(3)
list1.next = Node(1)
list1.next.next = Node(4)

list2 = Node(2)
list2.next = Node(5)
list2.next.next = Node(6)

merged_list = link_linked_lists(list1, list2)

sorted_merged_list = merge_sort_linked_list(merged_list)

current = sorted_merged_list
while current is not None:
    print(current.data, end=" -> ")
    current = current.next