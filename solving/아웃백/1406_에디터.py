'''
https://www.acmicpc.net/problem/1406
'''
import sys
input = sys.stdin.readline

# result = list(input().strip())
# cursor = len(result)
# n = int(input())

# for _ in range(n):
#     temp = list(input().split())
#     command = temp[0]

#     if command == "L":
#         cursor = max(0, cursor - 1)
#     elif command == "D":
#         cursor = min(cursor + 1, len(result))
#     elif command == "B":
#         if cursor:
#             result.pop(cursor - 1)
#             cursor = max(0, cursor - 1)
#     else:
#         value = temp[1]
#         result.insert(cursor, value)
#         cursor += 1

# print(*result, sep="")

left_stack = list(input().strip())
right_stack = []
n = int(input())

for _ in range(n):
    temp = list(input().split())
    command = temp[0]

    if command == "L":
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command == "D":
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command == "B":
        if left_stack:
            left_stack.pop()
    else:
        left_stack.append(temp[1])

right_stack.reverse()

print(*(left_stack + right_stack), sep="")
