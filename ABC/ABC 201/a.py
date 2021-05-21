a = list(map(int, input().split()))
a1, a2, a3 = sorted(a)
if a3 - a2 == a2 - a1:
    print("Yes")
else:
    print("No")