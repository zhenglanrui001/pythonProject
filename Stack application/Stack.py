class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, value):
        self.items.append(value)
    def pop(self):
        if len(self.items) == 0:
            return "Error: This is a empty stack!"
        else:
            self.items.pop()
    def peek(self):
        if len(self.items) == 0:
            return "This is a empty stack!"
        else:
            return self.items[-1]
    def __str__(self):
        return "Stack: {}".format(self.__items)