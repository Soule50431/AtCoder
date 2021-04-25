n, m = map(int, input().split())

if m == 0:
    print(3**n)

nodes = [[] for _ in range(n+1)]
for i in range(n):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
print(nodes)