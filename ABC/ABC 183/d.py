n, w = map(int, input().split())

queries = [list(map(int, input().split())) for _ in range(n)]
waters = [0] * 3*10**5

for s, t, p in queries:
    # s -= 1
    # t -= 1
    waters[s] += p
    waters[t] -= p

for i in range(len(waters)-1):
    waters[i+1] += waters[i]
# print(waters)

if max(waters) <= w:
    print("Yes")
else:
    print("No")
