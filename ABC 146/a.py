day = input()

days = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
print(days[-1::-1].index(day) +1)