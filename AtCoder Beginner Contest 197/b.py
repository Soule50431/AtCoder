h, w, x, y = map(int,input().split())
x -= 1
y -= 1

s = [input() for _ in range(h)]
# print(h,  w, x, y)
# print(s)

count = 1

# 左
for i in range(x-1,-1,-1):
    if s[i][y] == ".":
        count += 1
    else:
        break
# 右
for i in range(x+1, h):
    if s[i][y] == ".":
        count += 1
    else:
        break
# 上
for i in range(y-1, -1, -1):
    if s[x][i] == ".":
        count += 1
    else:
        break
# 下
for i in range(y+1, w):
    if s[x][i] == ".":
        count += 1
    else:
        break

print(count)