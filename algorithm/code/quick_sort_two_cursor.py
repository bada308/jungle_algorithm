def qsort(arr, left, right):
    pl = left
    pr = right
    x = arr[(left + right) // 2]
    
    while pl <= pr:
        while arr[pl] < x: pl += 1
        while arr[pr] > x: pr -= 1
        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
    
    if left < pr: qsort(arr, left, pr)
    if pl < right: qsort(arr, pl, right)

def quick_sort(arr):
    qsort(arr, 0, len(arr) - 1)

target = [3, 23, 4, 46, 19, 23, 50, 33]
quick_sort(target)
print(target)