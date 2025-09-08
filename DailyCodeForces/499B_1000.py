n, m = map(int, input().split())
lst = {}
for _ in range(m):
    a,b = map(str, input().split())
    lst[a] = b
s = list(map(str,input().split()))
result = []
for i in s:
    if i in lst:
        if len(i) > len(lst[i]):
            result.append(lst[i])
        else:
            result.append(i)
print(" ".join(result))