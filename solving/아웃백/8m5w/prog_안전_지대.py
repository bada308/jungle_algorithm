def solution(board):
    n = len(board)
    
    # 지뢰의 범위
    area = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    # 각 지역의 안전성 저장
    safe = [[1] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1: # 지뢰 발견 시 지뢰의 범위에 해당하는 지역의 안전성을 0으로 변경
                for di, dj in area:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        safe[ni][nj] = 0
    
    return sum(sum(s) for s in safe)