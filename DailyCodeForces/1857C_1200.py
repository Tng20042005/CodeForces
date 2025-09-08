t = int(input())
for _ in range(t):
    n = int(input())
    lst = sorted(list(map(int, input().split())))
    i = 0
    bn = n-1
    result = []
    while i< len(lst):
        result.append(lst[i])
        i += bn
        bn -= 1
    result.append(lst[-1])
    print(" ".join(map(str, result)))