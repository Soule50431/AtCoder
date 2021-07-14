import math
n, m = map(int, input().split())
if m == 0:
    print(1)
    exit()

a = list(map(int, input().split()))
a.sort()
a.insert(0, 0)
a.append(n+1)

between = [a[i+1] - a[i] - 1 for i in range(m+1)]
if all([num == 0 for num in between]):
    print(0)
    exit()
k = min([num for num in between if num != 0])

ans = 0
for i in range(m+1):
    ans += math.ceil((a[i+1] - a[i] - 1) / k)
print(ans)
