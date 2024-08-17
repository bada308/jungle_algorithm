'''
from collections import deque

def solution(n, results):
    answer = 0
    reach = [set() for _ in range(n+1)]
    
    graphA = dict()
    graphB = dict()
    
    for result in results:
        a, b = result
        if a in graphA:
            graphA[a].append(b)
        else:
            graphA[a] = [b]
        if b in graphB:
            graphB[b].append(a)
        else:
            graphB[b] = [a]
    
    for node in graphA:
        visited = [False] * (n+1)
        queue = deque(graphA[node])
        visited[node] = True
        reach[node].update(graphA[node])
        while queue:
            x = queue.popleft()
            if x in graphA and not visited[x]:
                queue.extend(graphA[x])
                reach[node].update(graphA[x])
            visited[x] = True

    
    for node in graphB:
        visited = [False] * (n+1)
        queue = deque(graphB[node])
        visited[node] = True
        reach[node].update(graphB[node])
        while queue:
            x = queue.popleft()
            if x in graphB and not visited[x]:
                queue.extend(graphB[x])
                reach[node].update(graphB[x])
            visited[x] = True
    
    for r in reach:
        if len(r) == n-1:
            answer += 1
    return answer
'''
from collections import deque, defaultdict

def solution(n, results):
    answer = 0
    
    # reach: 각 노드가 도달할 수 있는 노드 저장
    reach = [set() for _ in range(n+1)]
    
    # 정방향, 역방향에 해당하는 그래프 생성
    graphA, graphB = defaultdict(list), defaultdict(list)
    
    for a, b in results:
        graphA[a].append(b)
        graphB[b].append(a)
    
    # bfs 순회하면서 reach에 추가하는 함수
    def bfs(graph, start):
        visited = [False] * (n+1)
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    reach[start].add(neighbor)
                    queue.append(neighbor)
    
    for i in range(1, n+1):
        bfs(graphA, i)
        bfs(graphB, i)
    
    # 본인을 제외한 모든 노드에 도달할 수 있는 노드가 있으면 answer 증가
    for r in reach:
        if len(r) == n-1:
            answer += 1
    
    return answer