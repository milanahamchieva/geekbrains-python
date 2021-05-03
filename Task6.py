a, b = int(input()), int(input())
day = 1
while a <= b:
    a += a * 10 / 100
    day += 1
print(day)
