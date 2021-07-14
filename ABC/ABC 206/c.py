from collections import Counter
n = int(input())
a = list(map(int, input().split()))

a_counter = Counter(a)

sum_ = 0
for i in a_counter:
    sum_ += a_counter[i]

ans = 0
for i in a_counter:
    ans += a_counter[i] * (sum_ - a_counter[i])
print(ans//2)
