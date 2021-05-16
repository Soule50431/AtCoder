import numpy as np
n = int(input())
s = []
t = []

for i in range(n):
    s_, t_ = input().split()
    s.append(s_)
    t.append(int(t_))

idx = np.argmax(t)
t[idx] = 0
idx = np.argmax(t)
print(s[idx])