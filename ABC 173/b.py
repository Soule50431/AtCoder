from collections import Counter

n = int(input())

counter = Counter()
for i in range(n):
    s = input()
    counter[s] += 1

print("AC x", counter["AC"])
print("WA x", counter["WA"])
print("TLE x", counter["TLE"])
print("RE x", counter["RE"])
