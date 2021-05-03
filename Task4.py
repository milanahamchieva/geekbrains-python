n = int(input())
m = 0
while n:
    i = n % 10
    n //= 10
    if i > m:
        m = i
print(m)
