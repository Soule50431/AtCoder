n = int(input())

a = set()
b = set()

for i in range(n):
    s = input()
    if s[0] == "!":
        a.add(s[1:])
    else:
        b.add(s)

intersection = a & b
if len(intersection) == 0:
    print("satisfiable")
else:
    print(intersection.pop())
