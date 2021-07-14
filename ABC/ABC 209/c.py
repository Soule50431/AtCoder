n = int(input())
c = list(map(int, input().split()))
c = sorted(c)

MOD = 10**9 + 7
ans = 1

i = 0
for ci in c:
    ans = (ans * (ci - i)) % MOD
    i += 1
print(ans)
