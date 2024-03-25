# https://www.acmicpc.net/problem/18258

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0
        
    def is_empty(self):
        return self.front == None
    
    def getSize(self):
        return self.size
    
    def getFront(self):
        if self.is_empty():
            return -1
        return self.front.data
    
    def getRear(self):
        if self.is_empty():
            return -1
        return self.rear.data
    
    def enqueue(self, value):
        new_node = Node(value)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            return -1
        
        delete_node = self.front
        
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = delete_node.next
        
        self.size -= 1
        return delete_node.data


n = int(input())
queue = Queue()
answer = []

for _ in range(n):
    user_input = input().split()
    
    command = user_input[0]
    value = None
    
    if len(user_input) == 2:
        value = int(user_input[1])
    
    if command == "push":
        queue.enqueue(value)
    elif command == "pop":
        answer.append(queue.dequeue())
    elif command == "size":
        answer.append(queue.getSize())
    elif command == "empty":
        result = queue.is_empty()
        if result:
            answer.append(1)
        else:
            answer.append(0)
    elif command == "front":
        answer.append(queue.getFront())
    elif command == "back":
        answer.append(queue.getRear())

print(*answer, sep="\n")