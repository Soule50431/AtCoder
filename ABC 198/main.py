from heapq import *

# n = 3
# l = [1, 2, 3, 4, 5, 6]
# n = 4
# l = [1, 4, 5, 8, 7, 6, 3, 2]

n = int(input())
l = list(map(int, input().split()))
q = []

out = sum(l)
print(out)
for i in range(n-1, -1, -1):
    print(l)
    heappush(q, l[i])
    print(q)
    heappush(q, l[2*n-1-i])
    print(q)
    out -= heappop(q)
    print(out)