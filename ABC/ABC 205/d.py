from bisect import bisect_left

n, q = map(int, input().split())
a = list(map(int, input().split()))

num_list = [(a[i]-1) - i for i in range(n)]
# print(num_list)

for i in range(q):
    k = int(input())
    print(bisect_left(num_list, k) + k)