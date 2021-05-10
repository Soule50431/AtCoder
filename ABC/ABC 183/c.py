from itertools import permutations

n, k = map(int, input().split())

t = [list(map(int, input().split())) for i in range(n)]
# print(t)
count = 0
for comb in permutations((range(1, n))):
    prev = 0
    time = 0
    for town in comb:
        time += t[prev][town]
        prev = town
    time += t[town][0]

    if time == k:
        count += 1
print(count)
