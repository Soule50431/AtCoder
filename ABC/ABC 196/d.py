import itertools

h, w, a, b = map(int, input().split())

all_line = 2*h*w - h - w
# print(all_line)

seperate = w * (h-1)
count = 0

for comb in itertools.combinations(range(all_line), a):
    # print(comb)
    for i in comb:
        set_around = set()
        if i < seperate: # 横線を選択した時
            # print("横", i)

            if i-w >= 0: # 上
                # print(i-w)
                set_around.add(i-w)
            if i+w < seperate: # 下
                # print(i+w)
                set_around.add(i+w)
            if int(i%w) != 0: # 左
                # print(seperate + (i%w-1) * h + int(i/w), seperate + (i%w-1) * h + int(i/w)+1)
                set_around.add(seperate + (i%w-1) * h + int(i/w))
                set_around.add(seperate + (i%w-1) * h + int(i/w)+1)
            if int(i%w) != w-1: # 右
                # print(seperate+ i%w*h+ int(i/w), seperate+ i%w*h+int(i/w)+1)
                set_around.add(seperate+ i%w*h+ int(i/w))
                set_around.add(seperate+ i%w*h+int(i/w)+1)
        else: # 縦線
            # print("縦", i)

            if i - h >= seperate: # 左
                # print(i-h)
                set_around.add(i-h)
            if i+h < all_line: # 右
                # print(i+h)
                set_around.add(i+h)
            if int((i-seperate)%h) !=0 : # 上
                # print(((i-seperate)%h -1) * w + int((i-seperate)/h), ((i-seperate)%h -1) * w + int((i-seperate)/h)+ 1)
                set_around.add(((i-seperate)%h -1) * w + int((i-seperate)/h))
                set_around.add(((i-seperate)%h -1) * w + int((i-seperate)/h)+ 1)
            if int((i-seperate)%h) != h-1:# 下
                # print((i-seperate)%h * w + int((i-seperate)/h), (i-seperate)%h * w + int((i-seperate)/h)+ 1)
                set_around.add((i-seperate)%h * w + int((i-seperate)/h))
                set_around.add((i-seperate)%h * w + int((i-seperate)/h)+ 1)

        if not set_around.isdisjoint(set(comb)):
            # print(set(comb), set_around)
            break

    else:
        count += 1

print(count)
