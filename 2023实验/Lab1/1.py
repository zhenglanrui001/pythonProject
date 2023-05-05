class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked_List:
    def __init__(self):
        self.head = None
    def add(self, value):
        node1 = Node(value)
        node1.next = self.head
        self.head = node1

    def initlist(self, data_list):
        for word in data_list:
            self.add(word)

    def reverse(self):
        return self.head

    def print_list(self):
        print("linked_list:")
        current = self.head
        alist = []
        while current:
            alist.append(current.data)
            current = current.next
        print(alist)
