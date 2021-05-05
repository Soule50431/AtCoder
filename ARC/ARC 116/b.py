n = int(input())
a = sorted(list(map(int, input().split())))

ans = 0
s = 0
mod = 998244353

for ai in reversed(a):
    ans += ai**2
    ans += ai * s
    s = s*2 + ai
    ans %= mod
print(ans)
