import math

a, b, x = map(int, input().split())

if x <= a**2 * b / 2:
    theta = (math.pi / 2) - math.atan((2*x) / (b**2*a))
else:
    theta = math.atan((2*(a**2*b - x)) / a**3)
print(math.degrees(theta))