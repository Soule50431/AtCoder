n = int(input())

MOD = 10**9 + 7
print((pow(10, n, MOD) - 2 * pow(9, n, MOD) + pow(8, n, MOD))%MOD)