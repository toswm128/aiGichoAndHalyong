# def hello(message, name='User'):
#     print(f'{message} {name}')


# hello('abc', text="hihi")
# hello('def', text="bye")


# def int_sum(*a):
#     result = 0
#     for i in a:
#         if type(i) is int:
#             result += i

#     return result


# print(int_sum(1, 2, 3, 4, 5))
# print(int_sum(1, '2', True, "ads", 5))


def middle(list):
    i = len(list) // 2
    return list[i]


print(middle([1, 2, 3, 4, 5]))
print(middle([1, 2, 3, 4]))
