import calculator as c
import message

print(message.hello("민수"))

x = int(input("첫 번째 수: "))
y = int(input("두 번째 수: "))

print("덧셈: ", c.add(x, y))
print("뺄셈: ", c.subtract(x, y))
print("곱셈: ", c.multiply(x, y))
print("나눗셈: ", c.divide(x, y))
