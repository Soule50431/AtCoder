n = int(input())

ans = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    ans += (b-a+1) * (a + b) / 2
print(int(ans))