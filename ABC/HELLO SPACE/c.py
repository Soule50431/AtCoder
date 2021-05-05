n = int(input())
team = [tuple(map(int, input().split())) for i in range(n)]


def check(x):
    comb = set()
    for member in team:
        comb.add(sum(1 << i for i in range(5) if member[i] >= x))

    for x in comb:
        for y in comb:
            for z in comb:
                if x | y | z == 31:
                    return True
    return False


ok = 0
ng = 10**9 + 1

while ng - ok > 1:
    mid = (ng + ok) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)