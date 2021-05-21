s, t = input().split()
a, b = map(int, input().split())

u = input()

if u == t:
  print(a, b-1)
else:
  print(a-1, b)
