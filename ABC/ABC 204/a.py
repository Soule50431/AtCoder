x, y = map(int, input().split())

sum = x + y
if x == y:
    print(x)
    exit()

if sum == 1:
    print(2)
elif sum == 2:
    print(1)
else:
    print(0)
