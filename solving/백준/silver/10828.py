# https://www.acmicpc.net/problem/10828

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def getSize(self):
        return self.size
    
    def is_empty(self):
        return self.top == None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            return -1
        delete_node = self.top
        self.top = delete_node.next
        self.size -= 1
        
        return delete_node.data
    
    def getTop(self):
        if self.is_empty():
            return -1
        else:
            return self.top.data

n = int(input())
stack = Stack()

for _ in range(n):
    user_input = list(input().split())
    
    command = user_input[0]
    value = None
    if len(user_input) == 2:
        value = int(user_input[1])
    
    if command == "push":
        stack.push(value)
    elif command == "pop":
        print(stack.pop())
    elif command == "size":
        print(stack.getSize())
    elif command == "empty":
        if stack.is_empty():
            print(1)
        else:
            print(0)
    elif command == "top":
        print(stack.getTop())