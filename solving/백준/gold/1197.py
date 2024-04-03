'''
https://www.acmicpc.net/problem/1197
최소 스패닝 트리

MST 구하는 문제, 크루스칼로 해보장~~
'''

import sys
input = sys.stdin.readline

# 함수 영역
def find(x):
    if parent[x] == x:
        return parent[x]
    else:
        return find(parent[x])

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a == root_b:
        return False
    elif root_a < root_b:
        parent[root_b] = root_a
        return True
    else:
        parent[root_a] = root_b
        return True

def kruskal():
    result = 0
    
    for edge in edges:
        a, b, cost = edge
        
        if union(a, b):
            result += cost
    
    return result

# main

## 데이터 세팅
v, e = map(int, input().split())
edges = sorted([tuple(map(int, input().split())) for _ in range(e)], key=lambda x: x[2])
parent = [i for i in range(v+1)]

## 로직 실행
print(kruskal())
