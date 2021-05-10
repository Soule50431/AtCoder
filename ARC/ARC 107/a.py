a, b, c = map(int, input().split())
mod = 998244353

ans_a = (a * (a+1)) // 2
ans_b = (b * (b+1)) // 2
ans_c = (c * (c+1)) // 2

print((ans_a*ans_b*ans_c) % mod)
