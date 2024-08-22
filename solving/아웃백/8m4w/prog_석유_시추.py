from collections import deque

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# bfs를 이용해 석유 덩어리의 크기와 가로로 차지하는 구간 구하기
def bfs(land, visited, start_i, start_j):
    queue = deque([(start_i, start_j)])
    visited[start_i][start_j] = True
    count = 1
    j_set = set([start_j])
    
    while queue:
        i, j = queue.popleft()
        for di, dj in direction:
            ci, cj = i + di, j + dj
            if 0 <= ci < len(land) and 0 <= cj < len(land[0]) and land[ci][cj] == 1 and not visited[ci][cj]:
                queue.append((ci, cj))
                visited[ci][cj] = True
                count += 1
                j_set.add(cj)
    
    return count, j_set

def solution(land):
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    result = [0] * len(land[0]) # 수직으로 뚫었을 때 뽑을 수 있는 석유의 양 저장
    
    # 모든 위치 탐색
    for i in range(len(land)):
        for j in range(len(land[i])):
            # 석유가 있고 방문하지 않은 경우
            if land[i][j] == 1 and not visited[i][j]:
                count, j_set = bfs(land, visited, i, j)
                # result 배열에 석유 덩어리 크기 추가
                for jj in j_set:
                    result[jj] += count
                
    return max(result)

'''
from collections import deque

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def solution(land):
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    result = [0] * len(land[0])
    
    for i in range(len(land)):
        for j in range(len(land[i])):
            if land[i][j] == 1 and not visited[i][j]:
                j_set = set([j])
                count = 1
                queue = deque([(i, j)])
                visited[i][j] = True
                while queue:
                    ci, cj = queue.popleft()
                    for di, dj in direction:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < len(land) and 0 <= nj < len(land[0]) and land[ni][nj] == 1 and not visited[ni][nj]:
                            queue.append((ni, nj))
                            visited[ni][nj] = True
                            count += 1
                            j_set.add(nj)
                for jj in j_set:
                    result[jj] += count
                
    return max(result)
'''