import math
a, b, c, d = map(int, input().split())
if c * d - b != 0:
    n = a / (c * d - b)
else:
    n = -1
if n < 0:
    print(-1)
else:
    print(math.ceil(n))