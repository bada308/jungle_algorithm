# https://www.acmicpc.net/problem/11279

import sys
input = sys.stdin.readline

def heap_push(heap, value):
    heap.append(value)
    bubble_up(heap)

def bubble_up(heap):
    current = len(heap) - 1
    
    while current > 0:
        parent = (current - 1) // 2 
        
        if heap[parent] >= heap[current]:
            break
        heap[parent], heap[current] = heap[current], heap[parent]
        current = parent

def heap_pop(heap):
    if not heap:
        return 0
    if len(heap) == 1:
        return heap.pop()
    
    pop_data, heap[0] = heap[0], heap.pop()
    bubble_down(heap)
    
    return pop_data

def bubble_down(heap):
    current = 0
    child = 1
    
    while child < len(heap):
        sibling = child + 1
        
        if sibling < len(heap) and heap[child] < heap[sibling]:
            child = sibling
        
        if heap[current] >= heap[child]:
            break
        heap[current], heap[child] = heap[child], heap[current]
        current = child
        child = current * 2 + 1
        


n = int(input())
heap = []

for i in range(n):
    user_input = int(input())
    
    if user_input == 0:
        print(heap_pop(heap))
    else:
        heap_push(heap, user_input)