class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, x):
        new_node = Node(x)
        
        if self.front is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.front is None:
            return None
        
        delete_node = self.front
        
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        
        return delete_node.data
    
    def is_empty(self):
        return self.front is None