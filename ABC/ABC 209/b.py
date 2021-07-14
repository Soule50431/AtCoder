n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i, ai in enumerate(a):
    if (i+1) % 2 == 0:
        ans += ai -1
    else:
        ans += ai

if ans <= x:
    print("Yes")
else:
    print("No")