import math

n = int(input())

bill = math.ceil(n / 1000)
print(bill * 1000 - n)
