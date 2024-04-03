'''
https://www.acmicpc.net/problem/5639
이진 검색 트리

input : 전위 순회 결과
output : 후위 순회 결과

'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(2*10**5)

preorder = []

while True:
    try:
        preorder.append(int(input()))
    except:
        break

def postorder(arr):
    global result
    if len(arr) == 0:
        return
    if len(arr) == 1:
        result.append(arr[0])
        return
    
    pivot = arr[0]
    
    small = []
    large = []
    
    for a in arr:
        if a < pivot:
            small.append(a)
        elif a > pivot:
            large.append(a)

    postorder(small)
    postorder(large)
    result.append(pivot)


result = []

postorder(preorder)
print(*result, sep="\n")