import itertools
from operator import add
n, m, x = list(map(int, input().split()))

a = []
c = []
for i in range(n):
    temp = list(map(int, input().split()))
    c.append(temp[0])
    a.append(temp[1:])


min_ = float("INF")
for bits in itertools.product((True, False), repeat=n):
    algorithm = [0] * m
    money = 0
    for i, bit in enumerate(bits):
        if bit:
            algorithm = list(map(add, algorithm, a[i]))
            money += c[i]
    # print(algorithm)

    if all(elem >= x for elem in algorithm):
        # print(algorithm)
        # print(money)
        min_ = min(min_, money)

if min_ == float("INF"):
    print(-1)
else:
    print(min_)
