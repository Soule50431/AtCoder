from itertools import product
n, m = map(int, input().split())
constraints = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())
placement = [tuple(map(int, input().split())) for _ in range(k)]
# print(constraints, placement)

ans = 0
print(placement)
print(*placement)
for balls in product(*placement):
    print(balls)
# for choices in product((0, 1), repeat=k):
#     balls = [0] * (n + 1)
#     for i, choice in enumerate(choices):
#         balls[placement[i][choice]] = 1
#
#     count = 0
#     for constraint in constraints:
#         if balls[constraint[0]] > 0 and balls[constraint[1]] > 0:
#             count += 1
#
#     ans = max(ans, count)
# print(ans)
