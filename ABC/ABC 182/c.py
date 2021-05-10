from itertools import product
n = list(input())


def check(num):
    num = int("".join(num))

    if num % 3 == 0:
        return True
    else:
        return False


min_ = float("INF")
for comb in product((True, False), repeat=len(n)):
    if sum(comb) == len(n):
        continue
    s = []
    for i, bit in enumerate(comb):
        if not bit:
            s.append(n[i])
    if check(s):

        min_ = min(min_, sum(comb))
print(min_ if min_ != float("INF") else -1)


