n = int(input())

limit = [0]
for i in range(1, 5+2):
    limit.append(limit[i-1]*1000 + 999)
# print(limit)


count = 0
for comma in range(1, 5+1):
    temp = min(limit[comma+1]-limit[comma], n - limit[comma])
    count += temp * comma
    if limit[comma+1] >= n:
        break
print(max(count, 0))
