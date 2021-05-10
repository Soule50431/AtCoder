import math
import itertools

a, b = map(int, input().split())

# output = 0
#
# for x, y in itertools.combinations(range(A,B+1), 2):
#     gcd = math.gcd(x, y)
#     print(x, y, gcd)
#     if gcd > output:
#         output = gcd
#
# print(output)
gcd = 1
for c in reversed(range(1,b+1)):
    if math.ceil(a/c) < b//c:
        gcd = c
        break
print(gcd)