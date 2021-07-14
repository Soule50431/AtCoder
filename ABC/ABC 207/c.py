n = int(input())
segments = [list(map(int, input().split())) for _ in range(n)]


def get_segment(segment):
    ti, li, ri = segment

    if ti == 2:
        ri -= 0.1
    elif ti == 3:
        li += 0.1
    elif ti == 4:
        li += 0.1
        ri -= 0.1
    return li, ri


ans = 0
for i in range(n):
    for j in range(i+1, n):
        li, ri = get_segment(segments[i])
        # print(segments[i])
        # print(li, ri)
        lj, rj = get_segment(segments[j])
        # print(segments[j])
        # print(lj, rj)
        # print(i, j)
        # print(li, ri, lj, rj)
        if (li <= lj <= ri) or (lj <= li <= rj):
            # print(i, j)
            ans += 1
print(ans)
