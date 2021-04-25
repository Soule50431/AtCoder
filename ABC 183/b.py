sx, sy, gx, gy = list(map(int, input().split()))

ans = ((gx - sx)/(gy + sy)) * (sy + sx * ((gy + sy)/(gx - sx)))
print(ans)
