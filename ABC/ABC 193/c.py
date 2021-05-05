import math

n = int(input())

a_max = math.floor(math.sqrt(n))
# b_max = math.floor(math.log(n, 2))

# print(a_max, b_max)

seen_num = {}
for a in range(2, a_max+1):
    num = a * a
    while num <= n:
        seen_num[num] = 1
        num *= a
    # for b in range(2, b_max+1):
    #     if a**b <= n:
    #         seen_num[a**b] = 1
    #         pass
print(n - len(seen_num))
