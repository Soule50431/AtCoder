n, k = map(int, input().split())

friends = sorted([list(map(int, input().split())) for i in range(n)])
cur_village = 0

for a, b in friends:
    dist = a - cur_village
    if k - dist >= 0:
        k -= dist
        k += b
        cur_village += dist
    else:
        break
print(k + cur_village)

