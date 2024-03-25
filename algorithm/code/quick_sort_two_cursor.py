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


target = [3, 23, 4, 46, 19, 23, 50, 33]
qsort(target, 0, len(target) - 1)
print(target)