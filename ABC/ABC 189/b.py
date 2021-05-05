n, x = list(map(int, input().split()))

alcohol = 0

for i in range(1, n+1):
    v, p = list(map(int, input().split()))
    alcohol += v * p
    if alcohol > x * 100:
        print(i)
        exit()

print(-1)