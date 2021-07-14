p = int(input())

coins = [1] * 11
for i in range(1, 11):
    coins[i] *= i
    coins[i] *= coins[i-1]

ans = 0
for coin in reversed(coins[1:]):
    ans += p // coin
    p %= coin
print(ans)