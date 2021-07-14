from bisect import bisect_left

n, k = map(int, input().split())
a = list(map(int, input().split()))

a_sorted = sorted(a)
# print(a_sorted)
minimum = k // n
remain = k % n
# print(minimum, remain)

for ai in a:
    idx = bisect_left(a_sorted, ai)
    # print(idx)
    if idx + 1 <= remain:
        print(minimum+1)
    else:
        print(minimum)
