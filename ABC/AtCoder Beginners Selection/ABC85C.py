n, y = map(int, input().split())

for yukiti in range(n+1):
    # print(yukiti)
    for ichiyou in range(n-yukiti+1):
        hideyo = n - yukiti - ichiyou

        if 10000*yukiti + 5000*ichiyou + 1000*hideyo == y:
            # print(10000*yukiti + 5000*ichiyou + 1000*hideyo)
            print(yukiti, ichiyou, hideyo)
            exit()
print(-1, -1, -1)
