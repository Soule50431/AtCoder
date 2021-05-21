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


def check():
    for num in used:
        if used[num] > k:
            return False
    return True


used = Counter()

for i in range(4):
    used[int(s[i])] += 1
    used[int(t[i])] += 1

win = 0
count = 0
for i in range(1, 10):
    for j in range(1, 10):
        # print(i,j)
        used[i] += 1
        used[j] += 1
        if check():
            count += 1
            print(i, j, used)
        else:
            used[i] -= 1
            used[j] -= 1
            continue

        s_ = s.replace("#", str(i))
        t_ = t.replace("#", str(j))
        # print(s_, t_)
        takahashi = get_score(s_)
        aoki = get_score(t_)

        if takahashi > aoki:
            # print(takahashi, aoki)
            win += 1

        used[i] -= 1
        used[j] -= 1

print(win/count, win, count)