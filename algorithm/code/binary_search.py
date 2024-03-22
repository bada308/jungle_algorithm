def binary_search_recursion(arr, target):
    mid = len(arr) // 2
    
    if (arr[mid] > target):
        return binary_search_recursion(arr[:mid], target)
    elif (arr[mid] < target):
        return mid + binary_search_recursion(arr[mid:], target)
    else:
        return mid


def binary_search_recursion2(arr, target, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
        
    return binary_search_recursion2(arr, target, start, end)


def binary_search_loop(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        
    return -1


# 1~100 사이 길이 15의 정렬된 리스트
sorted_list = [2, 5, 26, 33, 34, 40, 88, 91, 99, 100]

print(binary_search_recursion(sorted_list, 26)) #2
print(binary_search_recursion(sorted_list, 34)) #4
print(binary_search_recursion(sorted_list, 88)) #6

print(binary_search_recursion2(sorted_list, 26, 0, len(sorted_list) - 1)) #2
print(binary_search_recursion2(sorted_list, 34, 0, len(sorted_list) - 1)) #4
print(binary_search_recursion2(sorted_list, 88, 0, len(sorted_list) - 1)) #6

print(binary_search_loop(sorted_list, 26)) #2
print(binary_search_loop(sorted_list, 34)) #4
print(binary_search_loop(sorted_list, 88)) #6