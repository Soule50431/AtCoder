n, m = map(int, input().split())

ok = set()
ok.add(n)

blacks = [list(map(int, input().split())) for i in range(m)]
blacks = sorted(blacks, reverse=True)

cur_line = set()
cur_line.add(n)
while blacks:
    delete_line = set()
    add_line = set()

    depth = blacks[-1][0]
    while blacks[-1][0] == depth:
        x, y = blacks.pop()
        # print("black", x, y)
        if y in cur_line:
            delete_line.add(y)

        if y-1 in cur_line:
            add_line.add(y)
        if y+1 in cur_line:
            add_line.add(y)
        if len(blacks) == 0:
            break
    cur_line.difference_update(delete_line)
    cur_line.update(add_line)
    # print(add_line, delete_line, cur_line)

# print(cur_line)
print(len(cur_line))