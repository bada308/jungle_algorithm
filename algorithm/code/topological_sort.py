import sys
from collections import deque
input = sys.stdin.readline

# 노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort(size):
    result = []
    queue = deque()
    
    for i in range(1, size + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        u = queue.popleft()
        result.append(u)
        
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return result


result = topology_sort(v)
print(result)

