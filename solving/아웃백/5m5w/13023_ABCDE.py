'''
https://www.acmicpc.net/problem/13023
'''
import sys
input = sys.stdin.readline

graph = {}


def dfs(curr, paths):
    if len(paths) == 5:
        print(1)
        exit(0)
    for x in graph[curr]:
        if x in paths:
            continue
        paths.add(x)
        dfs(x, paths)
        paths.remove(x)


# main
n, m = map(int, input().split())

for i in range(n):
    graph[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(n):
    dfs(i, set([i]))

print(0)
