import numpy as np
from itertools import combinations

def check(a, b, c, d, e):
    return min([max(a), max(b), max(c), max(d), max(e)])


n = int(input())

a = []
b = []
c = []
d = []
e = []

for i in range(n):
    a_, b_, c_, d_, e_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
    c.append(c_)
    d.append(d_)
    e.append(e_)

a = np.array(a)
b = np.array(b)
c = np.array(c)
d = np.array(d)
e = np.array(e)
# print(a, b, c, d, e)

if n == 3:
    print(check(a, b, c, d, e))
    exit()

a_idx = np.argmax(a)
b_idx = np.argmax(b)
c_idx = np.argmax(c)
d_idx = np.argmax(d)
e_idx = np.argmax(e)

check_list = list(set([a_idx, b_idx, c_idx, d_idx, e_idx]))
# print(check_list)
# print(a[check_list])
# if len(check_list) <= 3:
#     ans = check(a[check_list], b[check_list], c[check_list], d[check_list], e[check_list])
#     exit()
# elif len(check_list) == 4:
#     for comb in
#     exit()
# else:
#     exit()
max_ = 0
for comb in combinations(check_list, 3):
    comb = list(comb)
    max_ = max(max_, check(a[comb], b[comb], c[comb], d[comb], e[comb]))
print(max_)
