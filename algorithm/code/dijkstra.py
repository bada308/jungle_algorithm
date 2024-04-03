
import sys
input = sys.stdin.readline


# n: node 수, m: edge 수, k: 시작할 노드
n, m, k = map(int, input().split())
k = k-1

INF = 1e8

visited = [False for _ in range(n)]
distance = [INF for _ in range(n)]
graph = [[] for _ in range(n)]


for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u-1].append((v-1, cost))

def get_smallest_node():
    smallest = INF
    index = 0
    for i in range(n):
        if not visited[i] and smallest > distance[i]:
            smallest = distance[i]
            index = i
    return index

def dijkstra(start):
    # 초기 세팅
    distance[start] = 0
    visited[start] = True
    
    for i in graph[start]:
        distance[i[0]] = i[1]
    
    # 반복 시작
    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        
        for j in graph[now]:
            if distance[now] + j[1] < distance[j[0]]:
                distance[j[0]] = distance[now] + j[1]

dijkstra(k)
print(distance)
