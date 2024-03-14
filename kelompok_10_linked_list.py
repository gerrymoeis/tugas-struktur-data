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

   # CREATING AND UPDATING
    def create(self, data):
        node = Node(data, self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node

        if self.tail is None: self.tail = self.head
    
    def create_values(self, data_list):
        for data in data_list:
            self.create(data)
    
    def append(self, data):
        if self.head is None: return self.create(data)

        node = Node(data, prev=self.tail)
        self.tail.next = node
        self.tail = node
    
    def append_values(self, data_list):
        for data in data_list:
            self.append(data)
    
    def insert_at(self, data, index):
        if index < 0 or index >= self.length():
            raise Exception("Index out of Range")
        if index == 0: return self.create()
        if index == -1: return self.append()

        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                node = Node(data, temp.next, temp)
                temp.next.prev = node
                temp.next = node
                break
            temp = temp.next
            count += 1
    
    # DELETE OR REMOVING
    def delete(self):
        self.head = self.head.next
        self.head.prev = None

    def pop(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def remove_at(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Index out of Range")
        if index == 0: self.delete()

        count = 0
        node = self.head
        while node:
            if count == index - 1:
                node.next = node.next.next
                node.next.prev = node
            node = node.next
            count += 1
