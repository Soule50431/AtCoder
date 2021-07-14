n = int(input())

x = 1
while True:
    if x ** 2 + x >= 2 * n:
        break
    x += 1
print(x)