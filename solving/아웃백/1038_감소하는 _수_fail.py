'''
https://www.acmicpc.net/problem/1038
'''
import sys
input = sys.stdin.readline

table = [[1]*10]
table_count = [10]
limit = sum(table[0])  # 감소하는 수의 총 개수

# 10^i 번째 값이 k인 감소하는 수의 개수를 저장하는 테이블 채우기
for i in range(1, 10):
    temp = [0]
    for k in range(1, 10):
        temp.append(temp[k-1] + table[i-1][k-1])
    table.append(temp)
    table_count.append(sum(table[i]) + table_count[i-1])
    limit += sum(temp)
table_count = [0] + table_count[:-1]

print(*table, sep="\n")

n = int(input())

# 감소하는 수의 총 개수보다 큰 값이 들어오면 -1 리턴
if (limit <= n):
    print(-1)
    exit(0)

answer = 0

while n > 0:
    temp_num = 0
    for i in range(10):
        for j in range(10):
            # 누적 개수가 n보다 커진 경우 -> 10^i번째 값이 j인 감소하는 수 중에 찾는 값이 있다!!
            if temp_num + table[i][j] > n:
                answer += j * (10 ** i)
                # n 업데이트
                n -= temp_num
                if i > 0:
                    n += table_count[i-1]
                break
            # 누적 개수 더하기
            temp_num += table[i][j]
        if temp_num > n:  # 이중 for문을 탈출하기 위한 조건
            break


print(answer)
