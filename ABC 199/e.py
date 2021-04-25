import itertools
import math

n, m = map(int, input().split())
x = []
y = []
z = []

def check(a, x, y, z):
    bool = [True if a[i] <= y else False for i in range(x)]
    # print(bool)
    if sum(bool) <= z:
        return True
    else:
        return False

if m == 0:
    print(math.factorial(n))
    exit()

for i in range(m):
    x_, y_, z_ = map(int, input().split())
    x.append(x_)
    y.append(y_)
    z.append(z_)

count = 0
for a in itertools.permutations(range(1,n+1),n):
    if all([check(a[:x[i]], x[i], y[i], z[i]) for i in range(m)]):
        count += 1
print(count)