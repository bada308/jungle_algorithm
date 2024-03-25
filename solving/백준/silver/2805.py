# https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline

def calcTree(arr, height):
    result = 0
    for t in arr:
        if t > height:
            result += (t - height)
    return result

n, target = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)


sum = 0

while start <= end:
    mid = (start + end) // 2
    sum = calcTree(tree, mid)
    if sum > target:
        start = mid + 1
    elif sum < target:
        end = mid - 1
    else:
        break

if(sum < target):
    print(mid - 1)
else:
    print(mid)