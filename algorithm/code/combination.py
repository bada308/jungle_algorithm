def combination(arr, size):
    arr = sorted(arr)
    result = []
    
    def generate(chosen):
        if len(chosen) == size:
            result.append(chosen)
            return
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for next in range(start, len(arr)):
            chosen.append(arr[next])
            generate(chosen)
            chosen.pop()
    generate([])
    return result

print(combination([1, 2, 3, 4, 5], 3))