'''
https://www.acmicpc.net/problem/1991
트리 순회
'''

import sys
input = sys.stdin.readline

n = int(input())

tree = {}
start = None

for _ in range(n):
    root, left, right = input().strip().split()
    if start is None: start = root
    if left == ".": left = None
    if right == ".": right = None
    tree[root] = [left, right]

def 전위(node):
    if node is None:
        return
    print(node, end="")
    전위(tree[node][0])
    전위(tree[node][1])

def 중위(node):
    if node is None:
        return
    중위(tree[node][0])
    print(node, end="")
    중위(tree[node][1])

def 후위(node):
    if node is None:
        return
    후위(tree[node][0])
    후위(tree[node][1])
    print(node, end="")

전위(start)
print("")
중위(start)
print("")
후위(start)
print("")