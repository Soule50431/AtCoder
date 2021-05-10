a, b, c, k = map(int, input().split())

ans = 0
if k <= a:
    ans += k
elif k > a:
    ans += a

if 0 < k - a - b <= c:
    ans -= k - a - b

print(ans)