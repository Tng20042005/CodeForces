a, b = map(int, input().split())
total = a
while a//b > 0 :
    total += a // b
    a = a - a//b * b + a//b
print(total)