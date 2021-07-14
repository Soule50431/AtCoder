n = int(input())
a = list(map(int, input().split()))

ans = 0
for aa in a:
    ans += max(0, aa - 10)
print(ans)