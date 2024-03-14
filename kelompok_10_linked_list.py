class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self, data=None):
        self.head = Node(data) if data else None
        self.tail = self.head if data else None
        self.message = None

    # DISPLAYING VALUES
    def display(self, reversed=False):
        if self.head is None and self.tail is None:
            print(self.message) if self.message else print("Linked List is Empty")
            return
        linked_list = []

        if reversed:
            node = self.tail
            while node:
                linked_list.append(node.data)
                node = node.prev
        else:
            node = self.head
            while node:
                linked_list.append(node.data)
                node = node.next
        
        return linked_list

    def length(self):
        count = 0
        node = self.head

        while node:
            node = node.next
            count += 1

        return count
