x, y = map(int, input().split())

t = max(int((y - 2*x) / 2), 0)
c = max(int(x - t), 0)

# print(t,c)
if (2 * c + 4 * t) == y:
    print("Yes")
else:
    print("No")