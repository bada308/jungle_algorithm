class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
            
    def pop(self):
        if self.top is None:
            return None
        delete_node = self.top
        self.top = self.top.next
        return delete_node.data
        
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None


s = Stack()

for i in range(3):
    s.push(chr(ord("A") + i))
    print(f"Push data = {s.peek()}")
print()

while not s.is_empty():
    print(f"Pop data = {s.pop()}")
print()

print(f"Peek data = {s.peek()}")