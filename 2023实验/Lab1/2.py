class StackNode:
    def __init__(self):
        self.data = None
        self.next = None
class Stack:
    def __init__(self):
        self.__items = []
    def is_empty(self):
        return self.__items == []
    def push(self, item):
        self.__items.append(item)
    def pop(self):
        if len(self.__items) == 0:
            raise IndexError("ERROR: The stack is empty!")
        else:
            return self.__items.pop()
    def peek(self):
        if len(self.__items) == 0:
            raise IndexError("ERROR: The stack is empty!")
        else:
            return self.__items[len(self.__items) - 1]
class TestBM:
    def BracketMatch(self, str1):
        s = Stack()
        left = "{[("
        for char in str1:
            if char in left:
                s.push(char)
            else:
                if char == ")" and s.peek() == "(":
                    s.pop()
                elif char == "]" and s.peek() == "[":
                    s.pop()
                elif char == "}" and s.peek() == "{":
                    s.pop()
        print(s.is_empty())
