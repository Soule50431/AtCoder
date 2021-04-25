import numpy as np
n, m = map(int, input().split())
a = np.array(list(map(int, input().split())))

limit = np.sum(a) / (4 * m)

if np.sum(a >= limit) >= m:
    print("Yes")
else:
    print("No")