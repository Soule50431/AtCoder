n = int(input())

plans = [[0, 0, 0]] + [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    t, x, y = plans[i]
    t_, x_, y_ = plans[i+1]
    t = t_ - t
    distance = abs(x_ - x) + abs(y_ - y)
    # print(t, distance)
    if t < distance:
        print("No")
        exit()
    # print(t - distance )
    if (t - distance) % 2 == 1:
        print("No")
        exit()
print("Yes")
