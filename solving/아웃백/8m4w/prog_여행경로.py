from collections import defaultdict

def dfs(path, total, graph):
    if len(path) == total:
        return path
    curr = path[-1] 
    
    if graph[curr]: 
        for next in sorted(graph[curr]):
            print(next)
            path.append(next)
            graph[curr].remove(next)
            
            result = dfs(path, total, graph)
            if result: return result
            
            path.pop()
            graph[curr].append(next)

def solution(tickets):
    START = 'ICN'
    
    graph = defaultdict(list)
    for s, e in tickets:
        graph[s].append(e)
    
    return dfs([START], len(tickets) + 1, graph)