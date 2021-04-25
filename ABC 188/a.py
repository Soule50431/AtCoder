xy= list(map(int, input().split()))

if min(xy) + 3 > max(xy):
    print("Yes")
else:
    print("No")