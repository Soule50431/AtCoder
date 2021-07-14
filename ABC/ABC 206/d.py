n = int(input())

A = list(map(int, input().split()))

mid = len(A) // 2
max_num = 2*10**5+1

parents = [i for i in range(max_num)]
ranks = [0 for _ in range(max_num)]
# print(parents)


def find_root(x):
    if parents[x] == x:
        return x
    parents[x] = find_root(parents[x])
    return parents[x]

ans = 0
for i in range(mid):
    if find_root(A[i]) != find_root(A[n-1-i]):
        ans += 1
        a = A[i]
        b = A[n-1-i]

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
print(ans)
