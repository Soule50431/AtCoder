n = int(input())
a = list(map(int, input().split()))

ans = 0
for l in range(n):
    shortest = float("INF")
    for r in range(l,n):
        # print(l, r, length)
        shortest = min(shortest, a[r])
        ans = max(ans, shortest * (r-l+1))
        # print(length, ans)

print(ans)

# ans = 0
# for l in range(n):
#     length = 0
#     for r in range(l,n):
#         # print(l, r, length)
#         if a[l] <= a[r]:
#             length += 1
#         else:
#             length = 0
#         ans = max(ans, length * a[l])
#         # print(length, ans)
#
# print(ans)
