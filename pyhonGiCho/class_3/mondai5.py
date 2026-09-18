def solution():
    N = input()
    arr = list(map(str, input().split()))

    return sorted(arr, reverse=True)[0]


print(solution())
