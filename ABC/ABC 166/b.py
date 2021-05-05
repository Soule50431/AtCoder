n, k = map(int, input().split())

sunuke = set()

for i in range(k):
    d = int(input())
    for a in map(int, input().split()):
        sunuke.update([a])
print(n-len(sunuke))