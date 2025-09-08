n, m = map(int, input().split())
lst = list(map(int, input().split()))
c = 1
total = 0
for i in lst:
    if i >= c:
        total += i - c
        c = i
    else:
        total += n - c + i
        c = i
print(total)