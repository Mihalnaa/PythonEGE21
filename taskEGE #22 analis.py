# Дано:
x = int(input())
a = 0
b = 0
while x > 0:
    if x % 2 == 0:
        a += 1
    else:
        b += x % 10
    x = x // 10
print(a, b)
# Задание:
# Укажите наибольшее из таких чисел x, при вводе которого алгоритм печатает сначала 2, а потом 4.
