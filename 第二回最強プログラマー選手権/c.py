import math
import itertools

A, B = map(int, input().split())

output = 0

for x, y in itertools.combinations(range(A,B+1), 2):
    gcd = math.gcd(x, y)
    print(x, y, gcd)
    if gcd > output:
        output = gcd

print(output)