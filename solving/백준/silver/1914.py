# https://www.acmicpc.net/problem/1914

import sys
input = sys.stdin.readline


def hanoi(arr, start, target, other):
    # print(arr, start, target, other)
    if len(arr) == 1:
        move(start, target)
        return
    
    child = arr[:-1]
    parent = [arr[-1]]
    
    hanoi(child, start, other, target)
    hanoi(parent, start, target, other)
    hanoi(child, other, target, start)

def move(start, target):
    answer.append((start, target))



n = int(input())
answer = []

print(2**n - 1)
if (n <= 20):
    hanoi(list(range(1, n+1)), "1", "3", "2")
    for a in answer:
        print(a[0], a[1])