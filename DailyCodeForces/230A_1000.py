s, n = map(int, input().split())
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append([x, y])   

lst = sorted(lst, key=lambda d: d[0])
check = "YES"
for i in range(n):
    if s > lst[i][0]:
        s += lst[i][1]
    else:
        check = "NO"
        break
print(check)