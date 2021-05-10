n = int(input())
A = list(map(int, input().split()))

number = 0
gcd = 0

for i in range(2, 1000+1):
    count = 0
    for a in A:
        if a % i == 0:
            count += 1

    if count >= gcd:
        gcd = count
        number = i
        if gcd == len(A):
            break
print(number)