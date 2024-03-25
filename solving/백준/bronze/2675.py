# https://www.acmicpc.net/problem/2675

t = int(input())

for i in range(t):
    r, char = input().split()

    result = ""
    for c in char:
        result += (c * int(r))
    print(result)