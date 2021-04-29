r1, c1 = map(int, input().split())
r2, c2= map(int, input().split())

a = r2 - r1
b = c2 - c1

# print(a, b)

dist = abs(a) + abs(b)

if a == 0 and b == 0:
    print(0)
elif a + b == 0 or a - b == 0 or dist <= 3:
    print(1)
elif dist <= 6 or dist % 2 == 0 or abs(a-b) <= 3 or abs(a+b) <= 3:
    print(2)
else:
    print(3)