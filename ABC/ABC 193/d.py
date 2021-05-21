from collections import Counter

k = int(input())
s = input()
t = input()


def get_score(x):
    counter = Counter(x)
    score = 0
    for i in range(1, 10):
        score += i * (10**counter[str(i)])
    return score


cnt = [k] * 10
for i in range(4):
    cnt[int(s[i])] -= 1
    cnt[int(t[i])] -= 1

# print(cnt)
win = 0
count = 0
for i in range(1, 10):
    for j in range(1, 10):
        # print(i,j)
        if cnt[i] == 0:
            continue
        if i == j or cnt[j] == 0:
            continue

        s_ = s.replace("#", str(i))
        t_ = t.replace("#", str(j))
        # print(s_, t_)
        takahashi = get_score(s_)
        aoki = get_score(t_)

        if takahashi > aoki:
            win += cnt[i] * cnt[j]

for i in range(1,10):
    if cnt[i] < 2:
        continue
    s_ = s.replace("#", str(i))
    t_ = t.replace("#", str(i))
    # print(s_, t_)
    takahashi = get_score(s_)
    aoki = get_score(t_)

    if takahashi > aoki:
        win += cnt[i] * (cnt[i]-1)
# print(win)
print(win/(9*k-8)/(9*k-9))