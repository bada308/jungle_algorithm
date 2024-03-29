'''
DFS 파이썬으로 구현하기
'''

# 1. 재귀적으로 깊이 우선 탐색하기

graph1 = {1: [2, 3, 5], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [1, 4]} #무방향 그래프
graph2 = {1: [2, 3], 2: [3], 3: [4], 4: [], 5: [1, 4]}                 #방향 그래프

def dfs_recursive(graph, node):
    res = []
    visited = set()
    
    def _dfs(u):
        if u in visited:
            return
        res.append(u)
        visited.add(u)
        
        for v in graph[u]:
            if not v in visited:
                _dfs(v)
    _dfs(node)
    return res


print("무방향 그래프의 깊이 우선 탐색")
print("==========================")
print("노드 1에서 시작: ", dfs_recursive(graph1, 1))
print("노드 2에서 시작: ", dfs_recursive(graph1, 2))
print()
print("방향 그래프의 깊이 우선 탐색")
print("========================")
print("노드 1에서 시작: ", dfs_recursive(graph2, 1))
print("노드 2에서 시작: ", dfs_recursive(graph2, 2))

# 2. 스택을 이용하여 깊이 우선 탐색하기

def dfs(graph, node):
    res = []
    stack = [node]
    visited = set(stack)
    
    while stack:
        u = stack.pop()
        res.append(u)
        
        for v in graph[u]:
            if not v in visited:
                visited.add(v)
                stack.append(v)
    
    return res

print("무방향 그래프의 깊이 우선 탐색")
print("==========================")
print("노드 1에서 시작: ", dfs(graph1, 1))
print("노드 2에서 시작: ", dfs(graph1, 2))
print()
print("방향 그래프의 깊이 우선 탐색")
print("========================")
print("노드 1에서 시작: ", dfs(graph2, 1))
print("노드 2에서 시작: ", dfs(graph2, 2))