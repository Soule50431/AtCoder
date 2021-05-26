a, b = map(int, input().split())

s = f"{a}" * b
t = f"{b}" * a
if s < t:
    print(s)
else:
    print(t)