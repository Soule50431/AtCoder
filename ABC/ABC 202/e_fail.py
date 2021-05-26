import sys
sys.setrecursionlimit(10**6)

n = int(input())
p = list(map(int, input().split()))
edges = [[] for i in range(n)]
for i, pp in enumerate(p):
    i += 1
    pp -= 1
    edges[i].append(pp)
    edges[pp].append(i)
# print(edges)


def dfs(u, d):
    stack = [[0, -1, 0, u, d, False]]
    count = 0

    while stack:
        u, parent, depth, ui, di, flag = stack.pop()
        if u == ui:
            flag = True
        if depth == di:
            if flag:
                count +=1
        for child in edges[u]:
            if child == parent:
                continue
            stack.append([child, u, depth+1, ui, di, flag])
            # print(count, flag)

    return count


q = int(input())

for i in range(q):
    u, d = map(int, input().split())
    u -= 1
    ans = dfs(u, d)
    print(ans)

