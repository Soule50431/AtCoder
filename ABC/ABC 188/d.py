from collections import Counter

n, C = map(int, input().split())
costs = Counter()

for i in range(n):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    costs[a] += c
    costs[b+1] -= c


length = len(costs)
costs_list = sorted(costs)

for i in range(len(costs)):
    if i == 0:
        continue
    else:
        costs[costs_list[i]] += costs[costs_list[i-1]]

ans = 0
costs_list = sorted(costs)

for i, cost in enumerate(costs_list):
    # print(i)
    if i == length-1:
        continue
    height = min(C, costs[cost])
    width = costs_list[i+1] - costs_list[i]
    # print("costs", cost, costs[cost], height)
    # print("height width", height, width)
    ans += height * width
print(ans)



