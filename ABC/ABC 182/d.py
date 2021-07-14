n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
# print(a)
max_dist = [0] * len(a)

for i in range(len(a)-1):
    a[i+1] += a[i]
    max_dist[i+1] = max(a[i], max_dist[i])
# print(a)
# print(max_dist)
max_dist.append(0)
for i in range(len(a)-1):
    a[i+1] += a[i]
# print(a)

ans = 0
for i in range(len(a)):
    ans = max(ans, a[i] + max_dist[i+1])
print(ans)
