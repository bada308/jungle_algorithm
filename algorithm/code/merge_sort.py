import random

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
    
    
def merge(arr1, arr2):
    arr1_idx = arr2_idx = 0
    result = []
    
    while arr1_idx < len(arr1) and arr2_idx < len(arr2):
        if (arr1[arr1_idx] < arr2[arr2_idx]):
            result.append(arr1[arr1_idx])
            arr1_idx += 1
        else:
            result.append(arr2[arr2_idx])
            arr2_idx += 1
            
    if arr1_idx == len(arr1):
        result += arr2[arr2_idx:]
    else:
        result += arr1[arr1_idx:]
        
    return result



my_list = []
for _ in range(10):
    my_list.append(random.randrange(15))
    
    
print("정렬 전:")
print(my_list)
print()
print("정렬 후:")
my_list = merge_sort(my_list)
print(my_list)