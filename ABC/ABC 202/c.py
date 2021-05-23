from collections import Counter

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

bc = []
for cc in c:
    bc.append(b[cc-1])

a_counter = Counter(a)
bc_counter = Counter(bc)

ans = 0
for i in range(1, n+1):
    ans += a_counter[i] * bc_counter[i]
print(ans)