v, t, s, d = list(map(int, input().split()))

if d < v * t or d > v * s:
    print("Yes")
else:
    print("No")