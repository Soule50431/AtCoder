q = int(input())
n = 10**5
prime_numbers = [True] * (n + 1)
prime_numbers[0] = False
prime_numbers[1] = False

for i in range(2, n+1):
    if prime_numbers[i]:
        j = 2
        while i * j <= n:
            prime_numbers[i * j] = False
            j += 1

# for i, flag in enumerate(prime_numbers):
#     if flag:
#         print(i)

like2017 = [0] * (n + 1)
for i in range(n+1):
    if prime_numbers[i] and prime_numbers[(i+1) // 2]:
        like2017[i] = 1
print(like2017[:10])

s = [0] * (n+1)
for i in range(n):
    s[i+1] = s[i] + like2017[i]
print(s[:10])


for i in range(q):
    l, r = map(int, input().split())
    print(s[r+1] - s[l])

