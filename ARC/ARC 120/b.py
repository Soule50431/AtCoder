from collections import deque

h, w = map(int, input().split())
s = [input() for i in range(h)]

count = 0
blue = False
red = False
cur_depth = 0

queue = deque()
queue.append((0, 0, 0))
seen_node = set()

while queue:
    node = queue.popleft()
    x, y, depth = node
    if (x, y) in seen_node:
        continue
    seen_node.add((x, y))
    # queueに追加
    if x + 1 < h:
        if (x+1, y) not in seen_node:
            queue.append((x+1, y, depth+1))
    if y + 1 < w:
        if (x, y+1) not in seen_node:
            queue.append((x, y+1, depth+1))

    if cur_depth != depth:
        # 同じ深さを見終わった
        if not red and not blue:
            count += 1
        elif red and blue:
            print(0)
            exit()

        cur_depth = depth
        red = False
        blue = False

    color = s[x][y]
    if color == "R":
        red = True
    elif color == "B":
        blue = True
if s[h-1][w-1] == ".":
    count += 1
print(pow(2, count, 998244353))
