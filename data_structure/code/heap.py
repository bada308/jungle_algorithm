import heapq

def heappush(heap, data):
    heap.append(data)
    bubble_up(heap)

def bubble_up(heap):
    current = len(heap) - 1
    
    while current > 0:
        parent = (current - 1) // 2
        if (heap[parent] <= heap[current]):
            break
        heap[current], heap[parent] = heap[parent], heap[current]
        current = parent

def heappop(heap):
    if not heap:
        return "Empty Heap!"
    if len(heap) == 1:
        return heap.pop()
    
    pop_data, heap[0] = heap[0], heap.pop()
    bubble_down(heap)
    return pop_data

def bubble_down(heap):
    current, child = 0, 1
    
    while child < len(heap):
        sibling = child + 1
        
        # 자식끼리 비교
        if (sibling < len(heap) and heap[child] > heap[sibling]):
            child = sibling
        
        if (heap[child] >  heap[current]):
            break
        heap[child], heap[current] = heap[current], heap[child]
        current = child
        child = current * 2 + 1


def heapify(arr):
    current = start = len(arr) - 1
    
    while start > 0:
        is_swaped = False
        
        while current > 0:
            parent = (current - 1) // 2
            if arr[parent] < arr[current]:
                break
            arr[parent], arr[current] = arr[current], arr[parent]
            current = parent
            is_swaped = True
            
            
        if is_swaped:
            current = start
        else:
            current = start = current - 1
            
            

print("##heappush##")
h1 = [3, 4, 6, 8, 5, 7]
h2 = [3, 4, 6, 8, 5, 7]
heappush(h1, 2)
heapq.heappush(h2, 2)
print(f"힙 {h1}에 2를 추가한 결과")
print("구현한 함수의 결과: ", h1)
print("heapq 메서드의 결과:", h2)
print()
heappush(h1, 3)
heapq.heappush(h2, 3)
print(f"힙 {h1}에 3을 추가한 결과")
print("구현한 함수의 결과: ", h1)
print("heapq 메서드의 결과:", h2)


print("##heappop##")
h1 = [3, 4, 6, 8, 5, 7]
h2 = [3, 4, 6, 8, 5, 7]
print(f"힙 {h1}에서 pop한 결과\n")
data1 = heappop(h1)
data2 = heappop(h2)
print("구현한 함수 pop data =", data1)
print("구현한 함수 pop 이후: ", h1)
print()
print("heapq 함수 pop data =", data2)
print("heapq 함수 pop 이후: ", h2)

print("##heapify##")
h1 = [5, 2, 4, 1, 3]
h2 = [5, 2, 4, 1, 3]
heapq.heapify(h1) #내장 모듈의 함수를 이용한 것
heapify(h2)       #직접 구현한 것
print(f"내장 함수의 결과: {h1}")
print(f"구현 함수의 결과: {h1}")