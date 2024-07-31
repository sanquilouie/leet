class Node:
  def __init__(self,data):
    self.data = data
    self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = None

    def peek(self):
        return self.top.data

    def push(self, data):
        new_node = Node(data)
        if self.bottom is None:
            self.bottom = new_node
            self.top = self.bottom
            self.length = 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.length += 1

    def pop(self):
        pass


s = Stack()

s.push(6)
s.push(5)
print(s.peek())
