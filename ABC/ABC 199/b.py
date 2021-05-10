n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
# print(a, b)

number = set(list(range(a[0], b[0]+1)))
# print(number)
for i in range(1, n):
    temp = set(list(range(a[i], b[i]+1)))
    number = number & temp
print(len(number))