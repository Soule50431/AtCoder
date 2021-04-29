n, a, b = map(int, input().split())

a_b = n // (a + b)
left = n - (a+b) * a_b
# print(a_b, left)

ans = a * a_b

if a <= left:
    ans += a
elif a > left:
    ans += left

print(ans)
