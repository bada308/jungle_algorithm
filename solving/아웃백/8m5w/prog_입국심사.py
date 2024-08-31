def solution(n, times):
    start, end = 0, max(times) * n
    while start <= end:
        mid = (start + end) // 2
        count = sum([mid // i for i in times])
        # 심사 받는 사람이 n보다 적으면 시간이 불충분하다는 의미 -> start 늘리기
        if count < n:
            start = mid + 1
        # 많거나 같으면 시간이 널널하다는 의미 -> end 줄이기
        else:
            end = mid - 1
    return start