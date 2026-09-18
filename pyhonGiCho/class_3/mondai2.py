def solution():
    n = input()
    arr = list(map(int, input().split()))
    a = 0
    resultArr = []
    for i in arr:
        if i % 2 == 1:
            a += i
            resultArr.append(i)

    return '{0} {1}'.format(a, len(resultArr))


print(solution())
