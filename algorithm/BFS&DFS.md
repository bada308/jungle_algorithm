# DFS / BFS

## DFS

그래프 깊이 우선 탐색
: 특정 노드에서 시작하여 다음 분기(branch)로 넘어가기 전에 해당 분기를 **끝까지** 탐색하는 방법

- 스택(Stack) 자료구조 이용
- 재귀 함수 이용
- 인접 행렬로 구현하는 경우 시간복잡도는 O(V^2), 인접 리스트로 구현하는 경우 O(V+E)

### 파이썬으로 DFS 구현

[바로가기](./code/dfs.py)

## BFS

그래프 너비 우선 탐색
: 특정 노드에서 시작하여 인접한 노드를 먼저 탐색하는 방법

- 큐(Queue) 자료구조 이용
- 인접 행렬로 구현하는 경우 시간복잡도는 O(V^2), 인접 리스트로 구현하는 경우 O(V+E)

### 파이썬으로 BFS 구현

[바로가기](./code/bfs.py)
