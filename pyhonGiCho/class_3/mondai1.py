def solution():
    a, b, c = map(int, input().split())
    return sorted([a, b, c])[1]


print(solution())
