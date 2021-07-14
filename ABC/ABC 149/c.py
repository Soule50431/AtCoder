x = int(input())

max_num = 2*10**5
is_prime = [True] * max_num

for i in range(2, max_num):
    if is_prime[i]:
        j = 2
        while i * j < max_num:
            is_prime[i*j] = False
            j += 1

for i in range(x, max_num):
    if is_prime[i]:
        print(i)
        exit()
