import math

L, R = map(int, input().split())

ans = 0
g = 2
while g ** 2 <= 10**6:
    l, r = math.ceil(L/g), math.floor(R/g)
    if r - 1 == 1:
        break
    for i in range(l, r):
        ans += (r - i) - (math.floor(r / i) - 1)

    g += 1
print(ans*2)
