from collections import Counter
n, a, b = map(int, input().split())

line = ("b" * a + "r" * b)
print(line)
c = Counter(line[:n])
print(c["b"])