s = input()
t = input()

len_t = len(t)
count = len_t

for i in range(0,len(s)-len(t)+1):
    count_temp = 0
    for j in range(len_t):
        if t[j] != s[i:i+len_t][j]:
            count_temp += 1
    count = min(count, count_temp)
print(count)



# min_ = float("INF")
# len_t = len(t)
#
# for i in reversed(range(1, len(t))):
#     # print(i)
#     print("all", t[:i], t[i:])
#
#     idx = s.find(t[:i])
#     if idx != -1:
#         print("find")
#         print(t[idx+1+len(t[:i]):])
#         if len(t[idx+1+len(t[:i]):]) <= len(t[i:]):
#             min_ = min(min_, len(t[i:]))
#
#     idx = s.rfind(t[i:])
#     if idx != -1:
#         print("rfind")
#         print(t[:idx])
#         if len(t[:idx]) <= len(t[:i]):
#             min_ = min(min_, len(t[:i]))
#     # print("count", min_)
# print(min_)
