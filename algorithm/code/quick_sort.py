import random

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    
    left = []
    right = []
    
    for item in arr[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
            
    return quick_sort(left) + [pivot] + quick_sort(right)


my_list = []
for _ in range(10):
    my_list.append(random.randrange(15))
    
    
print("정렬 전:")
print(my_list)
print()
print("정렬 후:")
my_list = quick_sort(my_list)
print(my_list)