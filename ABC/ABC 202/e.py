from bisect import bisect_right, bisect_left
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

count = 0
depth_list = {}
euler_in = [0] * n
euler_out = [0] * n
in_ = 0
out = 0


def dfs(u, parent, depth):
    # 行きがけ
    global in_, out
    if depth not in depth_list:
        depth_list[depth] = [in_]
    else:
        depth_list[depth].append(in_)
    euler_in[u] = in_
    in_ += 1

    for child in edges[u]:
        if child == parent:
            continue
        dfs(child, u, depth+1)
    euler_out[u] = in_ - 1


dfs(0, -1, 0)
# print(euler_in)
# print(euler_out)

q = int(input())
for i in range(q):
    u, d = map(int, input().split())
    u -= 1
    # print(u, "depth", d)

    if d in depth_list:
        # print(cur_depth, euler_in[u], euler_out[u])
        # print(bisect_right(cur_depth, euler_out[u]))
        # print(bisect_left(cur_depth, euler_in[u]))
        print(bisect_right(depth_list[d], euler_out[u])- bisect_left(depth_list[d], euler_in[u]))
    else:
        print(0)

