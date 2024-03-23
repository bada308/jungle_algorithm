class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def __contains__(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            current = current.next
        
        return False
    
    def __str__(self):
        if self.head is None:
            return "Linked lise is empty!"
        res = "Head"
        node = self.head
        while node is not None:
            res += " → " + str(node.data)
            node = node.next
        return res
    
    def appendleft(self, x):
        new_node = Node(x)
        
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1

    
    def append(self, x):
        new_node = Node(x)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                node = node.next
            node.next = new_node
        
        self.length += 1
    
    def popleft(self):
        if self.head is None:
            return None
        
        delete_node = self.head
        self.head = self.head.next
        self.length -= 1
        
        return delete_node.data
    
    def pop(self):
        if self.head is None:
            return None

        delete_node = self.head
        while delete_node.next is not None:
            prev = delete_node
            delete_node = delete_node.next
        if delete_node == self.head:
            self.head = None
        else:
            prev.next = None
            
        self.length -= 1
        
        return delete_node.data
    
    def insert(self, i, x):
        if i <= 0:
            self.popleft(x)
        if i >= self.length:
            self.pop(x)
        else:
            current = self.head
            for i in range(i - 1):
                current = current.next
            new_node = Node(x)
            new_node.next = current.next
            current.next = new_node
            self.length += 1
    
    def remove(self, target):
        current = self.head
        
        while current is not None and current.data != target:
            prev = current
            current = current.next
        
        if current is None:
            return False
        if current == self.head:
            self.head = self.head.next
        else:
            prev.next = current.next
        
        self.length -= 1
        return True