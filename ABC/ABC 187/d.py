n = int(input())

votes = []
takahashi_voter = 0
aoki_voter = 0
for _ in range(n):
    a, b = map(int, input().split())
    aoki_voter += a
    votes.append([a, b, 2*a+b])

ans = 0
for vote in sorted(votes, key=lambda x:(x[2], x[0]), reverse=True):
    a, b, diff = vote

    if aoki_voter < takahashi_voter:
        break
    ans += 1
    aoki_voter -= a
    takahashi_voter += a + b

print(ans)