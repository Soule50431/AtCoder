n, q = map(int, input().split())

parents = [i for i in range(n)]
ranks = [0 for _ in range(n)]
# print(parents)


def find_root(x):
    if parents[x] == x:
        return x
    parents[x] = find_root(parents[x])
    return parents[x]


for _ in range(q):
    p, a, b = map(int, input().split())

    if p == 0: # 連結クエリ
        a_parent = find_root(a)
        b_parent = find_root(b)

        if a_parent == b_parent:
            continue

        if ranks[a_parent] < ranks[b_parent]:
            parents[a_parent] = b_parent
        else:
            parents[b_parent] = a_parent
            if ranks[a_parent] == ranks[b_parent]:
                ranks[a_parent] += 1

    else: # 判定クエリ
        if find_root(a) == find_root(b):
            print("Yes")
        else:
            print("No")
