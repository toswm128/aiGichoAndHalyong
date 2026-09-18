def solution():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []
    for i in arr:
        if i % K == 0:
            result.append(i)

    return " ".join(map(str, result))


print(solution())
