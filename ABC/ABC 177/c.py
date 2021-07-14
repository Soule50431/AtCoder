n = int(input())
a = list(map(int, input().split()))

a_ = [0] * n
for i in range(n-1):
    a_[i+1] += a_[i] + a[i]

ans = 0
MOD = 10**9 + 7
for i in range(n):
    ans = (ans + a_[i] * a[i]) % MOD
print(ans)