# https://www.acmicpc.net/problem/11866

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def is_empty(self):
        return self.front == None
    
    def enqueue(self, value):
        new_node = Node(value)
        
        if self.is_empty():
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        
    def dequeue(self):
        if self.is_empty():
            return
        
        delete_node = self.front
        
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        
        return delete_node.data

n, k = map(int, input().split())
queue = Queue()
answer = []

for i in range(1, n+1):
    queue.enqueue(i)

while(queue.is_empty() is False):
    for _ in range(k - 1):
        tmp = queue.dequeue()
        queue.enqueue(tmp)
    result = queue.dequeue()
    answer.append(result)

print("<", end="")
print(*answer, sep=", ", end="")
print(">")