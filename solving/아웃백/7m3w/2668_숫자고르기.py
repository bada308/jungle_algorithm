'''
https://www.acmicpc.net/problem/2668
'''
import sys
input = sys.stdin.readline

def dfs(cur, path):
    global answer
    next_num = nums[cur][1]
    if next_num in path: # 사이클 발견 시
        answer = answer | set(path[path.index(next_num):]) # 사이클에 포함된 숫자들을 answer에 추가
    else:
        visited[next_num] = True
        dfs(next_num, path + [next_num]) # 다음 숫자로 dfs 계속 진행
    


n = int(input())
nums = [(i, int(input()) - 1) for i in range(n)]
visited = [False] * n
answer = set([])

for idx, value in nums:
    if visited[idx]: # 이미 방문한 숫자라면 건너뜀
        continue
    if idx == value: # 숫자가 자기 자신을 가리키는 경우
        answer.add(idx) # 정답에 추가
        continue
    dfs(idx, [idx]) # dfs 탐색 시작

answer = list(answer)
answer.sort()
print(len(answer))
print(*list(map(lambda x: x + 1, answer)), sep="\n")



